![bts (2)](https://github.com/dldbfla/Image-Search-Down/assets/89433437/0070ef3b-fd80-4da7-8371-8b4cbe256e1e)
![bts (3)](https://github.com/dldbfla/Image-Search-Down/assets/89433437/cc14945a-0401-4b88-bfdd-be19fddf556f)
![bts](https://github.com/dldbfla/Image-Search-Down/assets/89433437/14e1357a-dac6-4496-b60d-024094df8222)

# Required Libraries:
PyQt5: GUI framework for the application interface.
requests: For making HTTP requests to the Google Custom Search API.
You can install these libraries via pip:



    pip install PyQt5 requests
# Key Notes:
API Key: Ensure you have a valid API key from Google to access the Custom Search JSON API. You can generate an API key in the Google Cloud Console.
Custom Search Engine ID: Set up a Custom Search Engine and note down the unique ID for image searches.
Limits and Quotas: Be aware of the API usage limits and quotas provided by Google. Usage beyond the limits might result in additional charges or restrictions.
Error Handling: Implement proper error handling for network requests and file operations. Ensure your code gracefully handles any potential errors during image downloads or API requests.
Folder Permissions: Ensure the application has permission to create directories and write files in the specified download folder. In certain operating systems, this might require elevated privileges.
Always be cautious with sensitive data like API keys and avoid sharing them in public code repositories or insecure channels. Keep your API keys secure and consider restricting access to prevent unauthorized usage.
