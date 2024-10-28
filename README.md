Notes:

-- Add Libraries to the requirments.txt file.

-- Make sure to enable "Microsoft.PolicyInsights" (Azure portal --> Subscriptions --> Settings --> Resource Providers -->  regester "Microsoft.PolicyInsights").

-- Apply for a VM quota for bigger models.

-- Standard vs Chat Prompt Flows.
  -chat can remember past conversations.

-- Endpoint test error temporary solution, Ddd the following code on any Python node:
  
    import os
    os.environ['PF_DISABLE_TRACING'] = 'true'

   Link: https://learn.microsoft.com/en-us/answers/questions/2082208/azure-ml-prompt-flow-qna-model-works-in-worskspace?comment=question#newest-question-comment
