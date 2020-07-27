# free-games-email-notifier
Code find free or on sale games and sends an email with the link

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and [npm](https://www.npmjs.com/) to install the libraries.

```bash
pip install requests
npm install dotenv
```
requests is used to get data from the websites.
dotenv is used to store sensitive information as an environment variable for safety.

## Usage
In the project folder make a .env file and store your sensitive information there. 
```API_Key=APIKey```, where APIKey is the sensitive information that you wish to hide.

The keys can then be used by ```os.getenv("NameOfVariable")``` in the code. Which in this case would be ```os.getenv("API_Key")```.

In my case, I have saved the emails of both the user who sends and those who will be receiving. Additionally, I need the password of the sender's email.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
