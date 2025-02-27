# OutStock <img src="https://github.com/horacehoff/outstock/blob/7e1b742f9223e2a245d03aab42a1611d5f59023f/guiAssets/outstock.ico" width="25">

This project allows you to save your files, no matter their size, on discords servers and retrieve them using a webhook on your server, as such everything runs locally.

All the files are stored on the discord server you set the webhook in, and the "history" file tracks the files, as such you can share it with anyone to allow them to download the files you uploaded.

```diff
- BEWARE !!!

- Do not delete the "history" file or the links to your files might be PERMANENTLY lost and 
- won't be able to be retrieved.
```

## Installation
- `pip install -r requirements.txt`
- Modify [webhook.py](./backend/webhook.py) and modify the webhook URL

## Screenshots
![App Screenshot](https://imgur.com/rGGIPz6.png)

## Contributing
Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

## Special thanks
We would like to thank Dev Detour and in particular, his [Stealing Storage from Discord](https://www.youtube.com/watch?v=c_arQ-6ElYI) video which inspired us to create this.

## License
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MIT_logo.svg/2880px-MIT_logo.svg.png" width="20"> [MIT License](LICENSE) \
Horace Hoff & Ulysse Coispellier - 2024
