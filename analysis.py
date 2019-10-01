# Analysis Example
# Send Notification to Yourself

# The main function used by Tago to run the script.
# It sends a notification to the account and another one linked to a dashboard.

# Environment Variables
# You must setup the following Environment Variables:
# message - Your Message
# title - Your Title
# ref_id - A bucket ID or a Dashboard ID.


from tago import Analysis
from tago import Services

# The function myAnalysis will run when you execute your analysis
def myAnalysis(context, scope):
  message = list(filter(lambda message: message['key'] == 'message', context.environment))
  message = message[0]['value']

  title = list(filter(lambda title: title['key'] == 'title', context.environment))
  title = title[0]['value']


  ref_id = list(filter(lambda ref_id: ref_id['key'] == 'dashboard;_id', context.environment))
  if not ref_id:
    ref_id = list(filter(lambda ref_id: ref_id['key'] == 'bucket_id', context.environment))
    if not ref_id:
      ref_id = None
    else:
      ref_id = ref_id[0]['value']
  else:
    ref_id = ref_id[0]['value']

  notification = Services(context.token).notification
  notification.send(title, message, ref_id)


# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('MY-ANALYSIS-TOKEN-HERE').init(myAnalysis)
