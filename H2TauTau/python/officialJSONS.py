prompt_2015 = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2.txt'


jsonMap = {
    # 2015
    '.*Run2015C.*':prompt_2015,
    '.*Run2015D.*':prompt_2015,
    }


if __name__ == '__main__':

    from CMGTools.RootTools.json.jsonPick import jsonPick

    samples = [
        '/SingleMuon/Run2015D-PromptReco-v4/MINIAOD',
        '/SingleMuon/Run2015D-05Oct2015-v1/MINIAOD',
        'root://eoscms.cern.ch//eos/cms/store/data/Run2015D/SingleMuon/MINIAOD/PromptReco-v4/000/258/159/00000/6CA1C627-246C-E511-8A6A-02163E014147.root'
        ]

    for sample in samples:
        print 'Sample', sample
        print '\tJSON    =', jsonPick( sample, jsonMap )
