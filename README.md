# Bildung 6.0

The website of the project Bildung 6.0, developed at Bern University of Applied Science.
https://www.bfh.ch/de/forschung/forschungsprojekte/2023-035-219-642/


## General Information:
Running MkDocs locally helps you preview changes as you edit the content in real time.

Using tools like Docker is recommended to avoid dependency issues. 

These tools encapsulate the necessary libraries, making it easier to manage projects with different requirements. 


For example, Docker images already include all required dependencies, so you don’t need to install anything separately.


## Using Docker

### Step 1: Clone Repository

Clone the project

```bash
  git clone https://github.com/bildung6/bildung6.git
```

Go to the project directory

```bash
  cd bildung6
```


---
### Step 2: Install Docker

You need to have docker installed.

- **Windows/macOS**:

  Download and install **Docker Desktop** from the official website (*During installation you may skip the registration*):

  --> https://www.docker.com/products/docker-desktop


- **Linux**:

  ```bash
  sudo apt update
  sudo apt install docker.io
  ```

---


### Step 3: Build and run Docker 

#### On M1, M2, Linux or Unix:


- **Go to the project directory:**
  ```bash
  cd bildung6
  ```

- **Pull the Required Docker Image** (*You need to pull the base Docker image*):
  ```bash
  docker pull squidfunk/mkdocs-material:latest
  ```


- **Build custom docker image** (*You need to build the custom docker image only once*):
  ```bash
  docker build -t mkdocs-material-custom .
  ```

- **Run the Docker container:**
  ```bash
  docker run --rm -it -p 8000:8000 -v ${PWD}:/docs mkdocs-material-custom
  ```

- **Navigate to the following URL in your browser:**
  http://0.0.0.0:8000/ or http://localhost:8000/


---

#### On Windows:

- **Go to the project directory:**
  ```bash
  cd bildung6
  ```


  - **Pull the required Docker image** (*You need to pull the base Docker image*):
  ```bash
  docker pull squidfunk/mkdocs-material:latest
  ```


- **Build custom Docker image** (*You need to build the custom docker image only once*):

  ```bash
  docker build -t mkdocs-material-custom .
  ```

- **Run the Docker container:**
  ```bash
  docker run --rm -it -p 8000:8000 -v "%cd%":/docs mkdocs-material-custom
  ```

- **Navigate to the following URL in your browser:**

  http://0.0.0.0:8000/ or http://localhost:8000/


---
---


## Directly via mkdocs without docker:

If you cannot or don't want to use Docker, you need to install the dependencies libraries first.

In that case we recommend to use an virtual environment like Conda.
If you prefer to install the libraries directly on your os then start on "Step 4: Install libraries".

---


### Step 1: Clone Repository

- **Clone the project:**
  ```bash
  git clone https://github.com/bildung6/bildung6.git
  ```

- **Go to the project directory:**
  ```bash
  cd bildung6
  ```


---


### Step 2: Install Conda

- Install Conda from hhttp.conda
- Install python & pip


---

### Step 3: Create Conda Environment


- **Create new Environment (only once):**
  ```bash
  conda create -n mkdocs_env python=3.9
  ```

- **Activate the Environment:**
  ```bash
  conda activate mkdocs_env
  ```

---

### Step 4: Install libraries

- **Install MkDocs and required libraries using pip:**
  ```bash
  pip install mkdocs-material mkdocs-mermaid2-plugin mkdocs-macros-plugin pymdown-extensions
  ```

---

### Step 5: Serve the MkDocs Site Locally

- **Navigate to your project folder::**
  ```bash
  cd bildung6
  ```

- **Serve the site:**
  ```bash
  mkdocs serve
  ```

- **Open your browser and visit:**
  Look at the terminal output and copy paste the URL into a browser.
  
  Use an URL from your Terminal output, which could look like this: 
   
  ```bash
  INFO    -  [12:41:36] Serving on http://127.0.0.1:8000/
  ```

---



## Authors

- [@nahakiole / Robin Glauser](https://github.com/nahakiole)
- [@d-reic / Daniel Reichenpfader](https://github.com/d-reic)
- [@dckbfh / Kerstin Denecke](https://github.com/dckbfh)
- [@denMo24/ Denis Moser ](https://github.com/denMo24)

## Contributing

Contributions are always welcome!


## Acknowledgements

- Amazing illustrations from [undraw.co](https://undraw.co/)
- A lot of inspiration taken from the home page of [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/)

## Feedback

If you have any feedback, please reach out to us at robin.glauser@bfh.ch

