# Table of Contents

1. [Prerequisites](#prerequisites)
2. [Overview](#overview)
3. [Step 1: Prepare Your Streamlit App](#step-1-prepare-your-streamlit-app)
   - [1.1 Create Your Streamlit App](#11-create-your-streamlit-app)
   - [1.2 Install Dependencies Locally (Optional)](#12-install-dependencies-locally-optional)
   - [1.3 Prepare `requirements.txt`](#13-prepare-requirementstxt)
4. [Step 2: Set Up Your GitHub Repository](#step-2-set-up-your-github-repository)
   - [2.1 Create a New Repository on GitHub](#21-create-a-new-repository-on-github)
5. [Step 3: Create and Upload Files to GitHub](#step-3-create-and-upload-files-to-github)
   - [3.1 Upload `app.py`](#31-upload-apppy)
   - [3.2 Create the `.streamlit` Directory and `config.toml`](#32-create-the-streamlit-directory-and-configtoml)
   - [3.3 Upload `requirements.txt`](#33-upload-requirementstxt)
   - [3.4 Create `startup.txt`](#34-create-startuptxt)
   - [3.5 Create the GitHub Actions Workflow File](#35-create-the-github-actions-workflow-file)
6. [Step 4: Configure Azure App Service](#step-4-configure-azure-app-service)
   - [4.1 Create a New Web App](#41-create-a-new-web-app)
   - [4.2 Configure Web App Settings](#42-configure-web-app-settings)
   - [4.3 Review and Create](#43-review-and-create)
   - [4.4 Configure Application Settings](#44-configure-application-settings)
7. [Step 5: Set Up GitHub Actions for Deployment](#step-5-set-up-github-actions-for-deployment)
   - [5.1 Obtain Azure Publish Profile](#51-obtain-azure-publish-profile)
   - [5.2 Add Publish Profile to GitHub Secrets](#52-add-publish-profile-to-github-secrets)
8. [Step 6: Deploy Your App](#step-6-deploy-your-app)
   - [6.1 Trigger the Deployment](#61-trigger-the-deployment)
   - [6.2 Monitor GitHub Actions](#62-monitor-github-actions)
9. [Step 7: Verify the Deployment](#step-7-verify-the-deployment)
   - [7.1 Access Your Web App](#71-access-your-web-app)
   - [7.2 Test Your App](#72-test-your-app)
10. [Step 8: Troubleshooting](#step-8-troubleshooting)
    - [8.1 Application Error Page](#81-application-error-page)
    - [8.2 Streamlit Command Not Found](#82-streamlit-command-not-found)
    - [8.3 Virtual Environment Activation](#83-virtual-environment-activation)
11. [Conclusion](#conclusion)
12. [Additional Notes](#additional-notes)

---

## Prerequisites

Before you begin, ensure you have the following:

- **Azure Account**: Access to an Azure subscription with permission to create resources.
- **GitHub Account**: A GitHub account to host your repository.
- **Streamlit App Files**: Your Streamlit app files ready on your local machine.

---

## Overview

This guide will help you deploy a Streamlit app to Azure App Service using GitHub (without Git commands) for continuous deployment. We'll:

- Organize your project files.
- Create and upload files to GitHub via the web interface.
- Set up Azure App Service.
- Configure GitHub Actions for automated deployment.
- Test and troubleshoot the deployment.

---

## Step 1: Prepare Your Streamlit App

### 1.1 Create Your Streamlit App

Develop your Streamlit app locally. For this guide, we'll assume your main app file is named `app.py`.

**Example `app.py`:**

```python
import streamlit as st

st.title("My Streamlit App")

st.write("Hello, world!")
```

### 1.2 Install Dependencies Locally (Optional)

While we'll manage dependencies via requirements.txt, you can test your app locally.

Install Streamlit (if you haven't already):

```bash
pip install streamlit
```

Run Your App Locally:

```bash
streamlit run app.py
```

Verify that your app works as expected.

### 1.3 Prepare `requirements.txt`

Create a requirements.txt file listing all the dependencies your app needs.

**Example `requirements.txt`:**

```
streamlit
```

If your app uses other packages (e.g., pandas, numpy), include them:

```
streamlit
pandas
numpy
```

---

## Step 2: Set Up Your GitHub Repository

'''
your-repo-name/
├── .github/
│   └── workflows/
│       └── azure-webapp.yml
├── .streamlit/
│   └── config.toml
├── app.py
├── requirements.txt
└── (Optional) startup.txt
'''

### 2.1 Create a New Repository on GitHub

Log in to GitHub: https://github.com

Create a New Repository:

- Click on the "+" icon in the top-right corner.
- Select "New repository".

**Repository Details:**

- Repository Name: [your-repo-name] (e.g., my-streamlit-app)
- Description: A brief description of your app.
- Public/Private: Choose according to your preference.
- Initialize this repository with:
  - Add a README file: Checked
  - Add .gitignore: Leave unchecked
  - Add a license: Leave as "None"

Click "Create repository".

---

## Step 3: Create and Upload Files to GitHub

We'll use the GitHub web interface to create directories and upload files.

### 3.1 Upload `app.py`

In your repository page, click on "Add file".

Select "Upload files".

Drag and drop your app.py file into the upload area, or click "choose your files" to select it.

**Commit Changes:**

- Commit message: "Add app.py"
- Commit directly to the main branch: Selected

Click "Commit changes".

### 3.2 Create the `.streamlit` Directory and `config.toml`

Create a New Directory:

On the repository page, click on "Add file".

Select "Create new file".

**Name the File:**

In the filename field, type `.streamlit/config.toml`.

Note: Typing a `/` creates a new directory.

**Add Content to `config.toml`:**

```toml
[server]
headless = true
enableCORS = false
port = 8000
enableXsrfProtection = false
address = "0.0.0.0"
```

**Commit Changes:**

- Commit message: "Add Streamlit config"
- Commit directly to the main branch: Selected

Click "Commit changes".

### 3.3 Upload `requirements.txt`

Click on "Add file" and select "Upload files".

Upload `requirements.txt`.

**Commit Changes:**

- Commit message: "Add requirements.txt"
- Commit directly to the main branch: Selected

Click "Commit changes".

### 3.4 Create `startup.txt` or configure azure

Create a New File:

Click on "Add file" and select "Create new file".

**Name the File:**

Type `startup.txt`.

**Add Content to `startup.txt`:**

```bash
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

**Commit Changes:**

- Commit message: "Add startup.txt"
- Commit directly to the main branch: Selected

Click "Commit changes".

(or)

Configure the Startup Command
- In your web app's menu, scroll down and click on "Configuration".

- Click on the "General settings" tab.

- Scroll down to find the "Startup Command" field.

- Enter the following command:
```
  streamlit run "Streamlit app/streamlit_app.py"
```

bash
Copy code
streamlit run "Streamlit app/streamlit_app.py"
Note: If your streamlit_app.py is directly inside the Streamlit app folder, this command points to it correctly.

Click on "Save" at the top to apply the changes.

### 3.5 Create the GitHub Actions Workflow File

Create Directories:

Click on "Add file" and select "Create new file".

**Name the File:**

Type `.github/workflows/azure-webapp.yml`.

**Add Content to `azure-webapp.yml`:**

```yaml
name: Build and Deploy to Azure Web App

on:
  push:
    branches:
      - main  # or your default branch

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout the code
        uses: actions/checkout@v2

      - name: Set up Python version
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'  # Match your app's Python version

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Archive files
        run: zip -r myapp.zip .

      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v2
        with:
          app-name: '[your-app-service-name]'  # Replace with your Azure Web App name
          slot-name: 'production'
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: 'myapp.zip'
```

**Commit Changes:**

- Commit message: "Add GitHub Actions workflow"
- Commit directly to the main branch: Selected

Click "Commit changes".

---

## Step 4: Configure Azure App Service

### 4.1 Create a New Web App

Log in to the Azure Portal: https://portal.azure.com

Create a New Resource:

- Click on "+ Create a resource".
- Search and Select "Web App":
  - Type "Web App" in the search bar.
  - Select "Web App" from the results.
  - Click "Create".

### 4.2 Configure Web App Settings

**Basics Tab:**

- Subscription: Select your Azure subscription.
- Resource Group: Create a new one or select an existing one (e.g., [your-resource-group]).
- Name: [your-app-service-name] (e.g., my-streamlit-app)
- Publish: Code
- Runtime Stack: Python 3.8 (or your app's Python version)
- Operating System: Linux
- Region: Choose a region close to your users (e.g., East US)

**App Service Plan:**

- Linux Plan: Create a new plan (e.g., [your-app-service-plan])
- SKU and Size: Choose B1 Basic (suitable for testing)

### 4.3 Review and Create

Review your settings.

Click "Create" to deploy the web app.

Wait for the deployment to complete.

### 4.4 Configure Application Settings

Navigate to Your Web App:

- Go to "Resource groups" in the left menu.
- Select your resource group.
- Click on your web app [your-app-service-name].

Go to Configuration:

- In the left menu, click on "Configuration".

Add Application Setting:

- Under "Application settings", click "New application setting".
- Name: `SCM_DO_BUILD_DURING_DEPLOYMENT`
- Value: `true`

Click "OK".

**Save Changes:**

Click "Save" at the top.

Confirm any prompts to apply the changes.

---

## Step 5: Set Up GitHub Actions for Deployment

### 5.1 Obtain Azure Publish Profile

Navigate to Your Web App in Azure Portal.

**Download Publish Profile:**

In the Overview section, click on "Get publish profile".

This will download a `.PublishSettings` file to your computer.

### 5.2 Add Publish Profile to GitHub Secrets

Go to Your GitHub Repository.

**Access Settings:**

Click on the "Settings" tab in your repository.

Navigate to Secrets:

- In the left sidebar, click on "Secrets and variables".
- Select "Actions".

**Add a New Secret:**

Click on "New repository secret".

- Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
- Value: Open the downloaded `.PublishSettings` file in a text editor and copy the entire content into the secret value.

Click "Add secret".

---

## Step 6: Deploy Your App

### 6.1 Trigger the Deployment

Since we've set up the GitHub Actions workflow to trigger on pushes to the main branch, we'll make a small change to trigger it.

**Edit the README (or any file):**

- On the repository page, click on the "README.md" file.
- Click the pencil icon to edit it.
- Add a line like "Deployment test".

**Commit Changes:**

- Commit message: "Trigger deployment"
- Commit directly to the main branch: Selected

Click "Commit changes".

### 6.2 Monitor GitHub Actions

Go to the "Actions" Tab:

- In your repository, click on "Actions".

**Monitor the Workflow:**

You should see a new workflow run in progress.

Click on it to see the detailed logs.

Wait for it to complete successfully.

---

## Step 7: Verify the Deployment

### 7.1 Access Your Web App

**URL:** `https://[your-app-service-name].azurewebsites.net`

Replace `[your-app-service-name]` with your actual app name.

### 7.2 Test Your App

Open the URL in a browser.

Verify that your Streamlit app is running and functioning correctly.

---

## Step 8: Troubleshooting

If you encounter issues, here are some common problems and solutions.

### 8.1 Application Error Page

**Cause:** The app failed to start correctly.

**Solution:**

- **Check Logs:**
  - In the Azure Portal, navigate to your Web App.
  - Click on "Log stream" in the left menu.
  - If prompted, enable application logging.
  - Look for error messages indicating the cause.

**Common Issues:**

- `ModuleNotFoundError`: Missing dependencies.
  - Ensure all dependencies are listed in `requirements.txt`.
- Port Binding Error: App not listening on the correct port.
  - Verify that `startup.txt` and `.streamlit/config.toml` specify port 8000.

### 8.2 Streamlit Command Not Found

**Cause:** The streamlit package is not installed.

**Solution:**

- Ensure streamlit is included in `requirements.txt`.
- Verify that the GitHub Actions workflow includes the step to install dependencies.

### 8.3 Virtual Environment Activation

**Note:** Azure's build process handles the virtual environment. You don't need to manually activate it.

---

## Conclusion

Congratulations! You've successfully deployed a Streamlit app to Azure App Service using GitHub without using Git commands. This setup allows you to automatically deploy updates by making changes directly in GitHub.

---

## Additional Notes

**Variable Placeholders:**

- `[your-repo-name]`: Your GitHub repository name.
- `[your-username]`: Your GitHub username.
- `[your-app-service-name]`: The name of your Azure Web App.
- `[your-resource-group]`: Your Azure Resource Group name.
- `[your-app-service-plan]`: Your Azure App Service Plan name.

**Scaling and Production:**

- For production use, consider scaling up your App Service Plan.
- Implement proper error handling and logging in your Streamlit app.

**Security:**

- Keep your Azure credentials secure.
- Do not expose sensitive information in your repository.
