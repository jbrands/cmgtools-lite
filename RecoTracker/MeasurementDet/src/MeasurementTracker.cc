#include "RecoTracker/MeasurementDet/interface/MeasurementTracker.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "Geometry/CommonDetUnit/interface/GeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/GluedGeomDet.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "DataFormats/SiStripCluster/interface/SiStripClusterCollection.h"
#include "TrackingTools/MeasurementDet/interface/MeasurementDetException.h"
#include "RecoTracker/TkDetLayers/interface/GeometricSearchTracker.h"
#include "RecoTracker/Record/interface/TrackerRecoGeometryRecord.h"
#include "RecoTracker/MeasurementDet/interface/TkStripMeasurementDet.h"
#include "RecoTracker/MeasurementDet/interface/TkPixelMeasurementDet.h"
#include "RecoTracker/MeasurementDet/interface/TkGluedMeasurementDet.h"
#include "RecoLocalTracker/SiPixelRecHits/interface/CPEFromDetPosition.h"
#include "RecoLocalTracker/ClusterParameterEstimator/interface/PixelClusterParameterEstimator.h"
#include "RecoLocalTracker/Records/interface/TrackerCPERecord.h"
#include "RecoLocalTracker/SiStripRecHitConverter/interface/SiStripRecHitMatcher.h"
#include "RecoLocalTracker/SiStripRecHitConverter/interface/StripCPE.h"  


#include <iostream>
#include <typeinfo>

MeasurementTracker::MeasurementTracker( const edm::EventSetup& setup, 
					const edm::ParameterSet& conf) :
  theTrackerGeom(0), stripCPE(0)
{
  using namespace std;
  this->initialize( setup, conf);

  cout << "MeasurementTracker: initialize OK" << endl;

}

void MeasurementTracker::initialize(const edm::EventSetup& setup, 
				    const edm::ParameterSet& conf)
{
  using namespace std;
    using namespace edm;
    edm::ESHandle<TrackerGeometry> pDD;
    setup.get<TrackerDigiGeometryRecord>().get( pDD );
    const TrackerGeometry& tracker(*pDD);
    theTrackerGeom = &tracker;

    cout << "MeasurementTracker::initialize: TrackerGeometry accessed" << endl; 

    const TrackerGeometry::DetContainer& dets = tracker.dets();

    std::cout << "got from TrackerGeometry " << dets.size() << std::endl; 

    // get pixelCPE
    //  ---- TEMPORARY SOLUTION TO COMMIT CODE FOR 070pre2   ----
    /*
    std::string cpeName = conf.getParameter<std::string>("PixelCPE");   
    cout <<" Asking for the CPE with name "<<cpeName<<endl;

    edm::ESHandle<PixelClusterParameterEstimator> pixelCPEHandle;
    setup.get<TrackerCPERecord>().get(cpeName,pixelCPEHandle);
    
    std::cout << "Got a pixelCPE " << typeid(*pixelCPEHandle).name() 
	      << std::endl;
    pixelCPE = &(*pixelCPEHandle);

    edm::ESHandle<MagneticField> magfield;
    setup.get<IdealMagneticFieldRecord>().get(magfield);
    */

    edm::ESHandle<MagneticField> magfield;
    setup.get<IdealMagneticFieldRecord>().get(magfield);
    edm::ParameterSet confPixelCPE;
    confPixelCPE.addParameter("TanLorentzAnglePerTesla",0.106);
    confPixelCPE.addUntrackedParameter("VerboseLevel",20);
    pixelCPE = new CPEFromDetPosition(confPixelCPE, &(*magfield));
    // -----------------------------------------------

    // get stripCPE
    edm::ESHandle<StripClusterParameterEstimator> stripCPEHandle;
    setup.get<TrackerCPERecord>().get("StripCPEfromTrackAngle",stripCPEHandle);

    std::cout << "Got a stripCPE " << typeid(*stripCPEHandle).name() 
	      << std::endl;
    stripCPE = &(*stripCPEHandle);

   
    theHitMatcher = new SiStripRecHitMatcher(conf);

    addPixelDets( tracker.detsPXB());
    addPixelDets( tracker.detsPXF());
    addStripDets( tracker.detsTIB());
    addStripDets( tracker.detsTID());
    addStripDets( tracker.detsTOB());
    addStripDets( tracker.detsTEC());

    edm::ESHandle<GeometricSearchTracker> gstrackerHandle;
    setup.get<TrackerRecoGeometryRecord>().get( gstrackerHandle);
    theGeometricSearchTracker = &(*gstrackerHandle);
}


void MeasurementTracker::addPixelDets( const TrackingGeometry::DetContainer& dets)
{
  for (TrackerGeometry::DetContainer::const_iterator gd=dets.begin();
       gd != dets.end(); gd++) {
      addPixelDet(*gd, pixelCPE);
  }  
}

void MeasurementTracker::addStripDets( const TrackingGeometry::DetContainer& dets)
{
  for (TrackerGeometry::DetContainer::const_iterator gd=dets.begin();
       gd != dets.end(); gd++) {

    const GeomDetUnit* gdu = dynamic_cast<const GeomDetUnit*>(*gd);

    //    StripSubdetector stripId( (**gd).geographicalId());
    //     bool isDetUnit( gdu != 0);
    //     cout << "StripSubdetector glued? " << stripId.glued() 
    // 	 << " is DetUnit? " << isDetUnit << endl;

    if (gdu != 0) {
      addStripDet(*gd, stripCPE);
    }
    else {
      const GluedGeomDet* gluedDet = dynamic_cast<const GluedGeomDet*>(*gd);
      if (gluedDet == 0) {
	throw MeasurementDetException("MeasurementTracker ERROR: GeomDet neither DetUnit nor GluedDet");
      }
      addGluedDet(gluedDet, theHitMatcher);
    }  
  }
}

void MeasurementTracker::addStripDet( const GeomDet* gd,
				      const StripClusterParameterEstimator* cpe)
{
  try {
    TkStripMeasurementDet* det = new TkStripMeasurementDet( gd, cpe);
    theStripDets.push_back(det);
    theDetMap[gd->geographicalId()] = det;
  }
  catch(MeasurementDetException& err){
    cout << "Oops, got a MeasurementDetException: " << err.what() << endl;
  }
}

void MeasurementTracker::addPixelDet( const GeomDet* gd,
				      const PixelClusterParameterEstimator* cpe)
{
  //cout << "pixelCPE in addPixelDet: " << cpe << endl; 
  TkPixelMeasurementDet* det = new TkPixelMeasurementDet( gd, cpe);
  thePixelDets.push_back(det);
  theDetMap[gd->geographicalId()] = det;
}

void MeasurementTracker::addGluedDet( const GluedGeomDet* gd,
				      SiStripRecHitMatcher* matcher)
{
  const MeasurementDet* monoDet = idToDet( gd->monoDet()->geographicalId());
  if (monoDet == 0) {
    addStripDet(gd->monoDet(), stripCPE);  // in case glued det comes before components
    monoDet = idToDet( gd->monoDet()->geographicalId());
  }

  const MeasurementDet* stereoDet = idToDet( gd->stereoDet()->geographicalId());
  if (stereoDet == 0) {
    addStripDet(gd->stereoDet(), stripCPE);  // in case glued det comes before components
    stereoDet = idToDet( gd->stereoDet()->geographicalId());
  }

  if (monoDet == 0 || stereoDet == 0) {
    std::cout << "MeasurementTracker ERROR: GluedDet components not found as MeasurementDets "
	      << endl;
    throw MeasurementDetException("MeasurementTracker ERROR: GluedDet components not found as MeasurementDets");
  }

  TkGluedMeasurementDet* det = new TkGluedMeasurementDet( gd, theHitMatcher,
							  monoDet, stereoDet);
  theGluedDets.push_back( det);
  theDetMap[gd->geographicalId()] = det;
}

void MeasurementTracker::update( const edm::Event& event) const
{
  typedef edm::DetSetVector<SiStripCluster> ::detset    StripDetSet;
  typedef edm::DetSetVector<SiPixelCluster> ::detset   PixelDetSet;

  // std::string clusterProducer = conf_.getParameter<std::string>("ClusterProducer");
  //std::string stripClusterProducer ("ClusterProducer"); // FIXME SiStripClusterizer
  std::string stripClusterProducer ("ThreeThresholdClusterizer");
  edm::Handle<edm::DetSetVector<SiStripCluster>> clusterHandle;
  event.getByLabel(stripClusterProducer, clusterHandle);
  const edm::DetSetVector<SiStripCluster>* clusterCollection = clusterHandle.product();

  //cout << "--- siStripClusterColl got " << endl;

  // loop over all strip dets
  for (std::vector<TkStripMeasurementDet*>::const_iterator i=theStripDets.begin();
       i!=theStripDets.end(); i++) {
    // foreach det get cluster range
    //    StripClusterRange range = clusterCollection->get( (**i).geomDet().geographicalId().rawId());


    unsigned int id = (**i).geomDet().geographicalId().rawId();
    const StripDetSet & detSet = (*clusterCollection)[ id ];
    (**i).update( detSet, clusterHandle, id );


    // push cluster range in det
    //    (**i).update( range );
  }
  //cout << "--- end of loop over dets" << endl;

  // Pixel Clusters
  std::string pixelClusterProducer ("pixClust"); 

  edm::Handle<edm::DetSetVector<SiPixelCluster>> pixelClusters;
  event.getByLabel(pixelClusterProducer, pixelClusters);
  const  edm::DetSetVector<SiPixelCluster>* pixelCollection = pixelClusters.product();
  //cout << "--- siPixelClusterColl got " << endl;

  for (std::vector<TkPixelMeasurementDet*>::const_iterator i=thePixelDets.begin();
       i!=thePixelDets.end(); i++) {
    // foreach det get cluster range
    unsigned int id = (**i).geomDet().geographicalId().rawId();
    const PixelDetSet & detSet = (*pixelCollection)[ id ];
    // push cluster range in det
    (**i).update( detSet, pixelClusters, id );
  }
  //cout << "--- end of loop over dets" << endl;

  /// or maybe faster: loop over all strip dets and clear them
  /// loop over dets with clusters and set range

}



const MeasurementDet* 
MeasurementTracker::idToDet(const DetId& id) const
{
  std::map<DetId,MeasurementDet*>::const_iterator it = theDetMap.find(id);
  if(it !=theDetMap.end()) {
    return it->second;
  }else{
    //throw exception;
  }
  
  return 0; //to avoid compile warning
}
