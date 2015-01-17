#Including the dropbox sdk
import dropbox

#Providing the app key and app secret.
app_key = 'nzy0jdjvmf8nf03'
app_secret = 'gmbfsgnz4zhec4e'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
