# Bildung 6.0

The website of the project Bildung 6.0 from the Berne University of Applied Science.
https://www.bfh.ch/de/forschung/forschungsprojekte/2023-035-219-642/

## Run Locally

Clone the project

```bash
  git clone https://github.com/bildung6/bildung6.git
```

Go to the project directory

```bash
  cd bildung6
```

Run mkdocs via docker or locally (https://squidfunk.github.io/mkdocs-material/creating-your-site/#previewing-as-you-write)


On M1/M2
```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs ghcr.io/afritzler/mkdocs-material 
```

On Linux / Unix
```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
```

On Windows
```bash
docker run --rm -it -p 8000:8000 -v "%cd%":/docs squidfunk/mkdocs-material
```

Directly via mkdocs
```bash
mkdocs serve
```
## Contributing

Contributions are always welcome!


## Acknowledgements

- [Illustrations](https://undraw.co/)
- [Mkdocs Material](https://squidfunk.github.io/mkdocs-material/)

## Feedback

If you have any feedback, please reach out to us at robin.glauser@bfh.ch

