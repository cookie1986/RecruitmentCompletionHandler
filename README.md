# Recruitment Completion Handler
This function receives user input from a Qualtrics survey, and then writes that data to a PostgreSQL instance held on Azure.


## Function Setup for Local Development

### Pre-requisites
- Python 3.x
- Azure Functions Core Tools
- jq JSON processor

### Installing jq (macOS)

Run ```brew install jq``` in your terminal.

### ARM64 Architecture Support
If you are running the project on a machine with ARM64 architecture, follow these steps to add local support:

1. Create a Makefile: Copy the ```/Makefile``` and store somewhere in your directory
2. Run the Makefile: Open your terminal and run the following command:

    ```make install_func_arm64_worker```

### Tunneling
Use a tunneling service to expose your localhost to the web temporarily for testing:

1. Go to the [Getting Started](https://ngrok.com/docs/getting-started/) section of the ngrok website.
2. Follow steps 1-2 to install ngrok and verify via ```ngrok -h```
3. Sign in to an ngrok account.
4. Start the service with ```ngrok http 7071```
5. Test the connection by entering the *forwarding* URL


### Setup Webhooks
To trigger webhooks from Qualtrics when a certain event has occurred (i.e., a survey has been completed), requires an active survey:

1. Go to [Qualtrics](www.qualtrics.com) and create a survey.
2. Go to the *survey flow* section and add a *new element* below the last question.
3. Select **Web Service** from the available options.
4. In the URL field, add the forwarded url endpoint.
5. Change the method from *GET* to *POST*
6. Add the appropriate parameters to the query or body of the API call, and select the correct question for the value field. 

### Testing Webhooks from Qualtrics Preview
Test the connection between Qualtrics and your function to make sure the webhook is performing as expected:

1. Preview your survey in Qualtrics.
2. Answer questions until you reach the web service point (i.e., the end of the survey)
3. In VS Code, go to the terminal where your function is running. Check the logs for **Python HTTP trigger function processed a request**, which indicates the request was successful.
4. [optional], if you want to view the output, add a print statement to main.py

## Deploy to Azure
Instructions for deploying a function app to Azure can be found [here](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions).

### Test connection to Qualtrics
Test the Qualtrics survey can connect to the function app by doing the following:

## Credits

ARM64 support for local development was implemented based on a solution provided in [this GitHub post](https://github.com/Azure/azure-functions-python-worker/issues/915#issuecomment-1552394117).
