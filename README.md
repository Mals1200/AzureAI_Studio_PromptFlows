# Azure AI Studio Prompt Flow README

## Overview

This document outlines the setup requirements and recommendations for utilizing Azure AI Studio Prompt Flow effectively. Follow the guidelines below to ensure your application integrates smoothly with Azure services and efficiently handles user interactions.

## Requirements

### 1. Update `requirements.txt`
- Ensure that all necessary libraries are included in your `requirements.txt` file. This allows for all functionalities needed by your application.

### 2. Enable Microsoft.PolicyInsights
- Navigate to the Azure Portal:
  - Go to **Subscriptions**.
  - Select **Settings**.
  - Under **Resource Providers**, register the **Microsoft.PolicyInsights** provider.

### 3. VM Quota for Larger Models
- If you plan to deploy larger models, apply for a VM quota increase in your Azure subscription settings.

## Prompt Flow Types

### Standard vs. Chat Prompt Flows
- **Chat Prompt Flows**:
  - Can remember past conversations.
  - Should include a list component to store previous user inputs.

#### Transformation from Standard to Chat Prompt Flow
- To transform a Standard Prompt Flow into a Chat Prompt Flow, follow the guidelines below. However, it's often easier to start fresh by selecting a Chat flow.

**Required Input**:  
Add an extra list input named `chat_history` with an initial value of `[]`.

**Example Code**:
```jinja
{% for item in chat_history %}
# user:
{{ item.inputs.question }}
# assistant:
{{ item.outputs.answer }}
{% endfor %}
```

Endpoint Testing Error - Temporary Solution
If you encounter errors when testing the endpoint, add the following code to any Python node to disable tracing temporarily:
in any python script node
```
import os
os.environ['PF_DISABLE_TRACING'] = 'true'
```
References
For additional information and troubleshooting, refer to the following link:


**consuming a chat input example Code**:
```jinja
    # Prepare chat history in the format expected by the API
    chat_history_list = [
        {"inputs": {"question": item["question"]}, "outputs": {"answer": item["answer"]}}
        for item in chat_history
    ]
    
    # Structure the data with 'question' and 'chat_history' as top-level keys
    data = {
        "question": question,
        "chat_history": chat_history_list  # Send all previous questions and answers in the correct format
    }
```
