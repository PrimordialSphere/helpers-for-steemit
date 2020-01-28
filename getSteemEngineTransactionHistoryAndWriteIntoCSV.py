from steemengine.api import Api
api = Api()

print(api.get_history("beerlover", "BEER"))