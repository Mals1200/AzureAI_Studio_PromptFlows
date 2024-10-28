Notes:

-- Add Libraries to the requirments.txt file.

-- Make sure to enable "Microsoft.PolicyInsights" (Azure portal --> Subscriptions --> Settings --> Resource Providers -->  regester "Microsoft.PolicyInsights").

-- Apply for a VM quota for bigger models.

-- Standard vs Chat Prompt Flows.
  - Chat can remember past conversations.
  - By adding a list component that store previouse user inputs.
  - refer to (Standard_to_Chat_code) below to transform a standard PF to  Chat PF. But its easier to start from scratch as a chat by selecting chat.

-- Endpoint test error temporary solution, Ddd the following code on any Python node:
  
    import os
    os.environ['PF_DISABLE_TRACING'] = 'true'

   Link: https://learn.microsoft.com/en-us/answers/questions/2082208/azure-ml-prompt-flow-qna-model-works-in-worskspace?comment=question#newest-question-comment




Standard_to_Chat_code, an extra type list input named "chat_history" with value "[]" is needed for the transformation to work.

  {% for item in chat_history %}
  # user:
  {{item.inputs.question}}
  # assistant:
  {{item.outputs.answer}}
  {% endfor %}
