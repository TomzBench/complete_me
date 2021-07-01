# def Settings( **kwargs ):
#     return { 'ls': {
#                 'checkOnSave' : { 'command' : 'clippy', 'allTargets': 'true'},
#                 'procMacro' : {
#                     'enable': True
#                 },
#                 'cargo' : {
#                     'loadOutDirsFromCheck': True,
#                     'runBuildScripts': True
#                     }
#                 },
#         }
# 
def Settings(**kwargs):
  if kwargs[ 'language' ] == 'rust':
    return {
        'ls': {
          'checkOnSave' : { 'command' : 'clippy', 'allTargets': 'true'},
          'procMacro': {"enable": True },
          'cargo': { 'loadOutDirsFromCheck': True, 'runBuildScripts': True },
          'experimental': { 'procAttrMacros': True }
        }
    }
