# Go Pro Web UI
![Screenshot of UI](docs/media/image.png)
## Usage
First clone the repository.
```bash
git clone "https://github.com/MrRyanPerson/GoPro-webui.git"

cd "GoPro-webui"
```
### Depedencies
```bash
# Restart terminal after running
winget install -e --id OpenJS.NodeJS

# Should return version of node and npm
node -v
npm -v
```
Enter the backend Directory
```bash
cd ./backend
```
Now, create a venv and activate it
```
python -m venv .venv

./.venv/Scripts/Activate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Enter project root directory and install dependencies
```bash
npm ci

npm run build
```
### Running
Program Commands
```bash
# Start the program. Program will be available at http://localhost:3000
npm run start

# Stop the program
npm run stop

# Delete all proccesses
npm run delete

# View logs
npm run monit
```
## Development
### 5/20/2026
* Started Project
* Initialized Project Structure and Svelte Project + Fastapi backend
### 5/21/2026
* Finalized UI for app
* Created Mock Backend.
### 5/22/2026
* Finished Backend.
## Wiki
[Link To Wiki](https://github.com/MrRyanPerson/GoPro-webui/wiki)
