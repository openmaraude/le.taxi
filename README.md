# Le.taxi

This is the Jekyll static website behind [https://le.taxi](https://le.taxi).

## Usage

Unlike most of le.taxi projects, this website has no dependencies so it is not integrated in [APITaxi_devel](https://github.com/openmaraude/APITaxi_devel). To run the project locally using Docker, run `make`. Go to [http://localhost:4000](http://localhost:4000) to view the website.

Code is mounted as a Docker volume, so any change on the host reloads the web server.

If you need a shell in the container, you can also run `make shell` then run the server by calling the default entrypoint: `/usr/local/bin/docker-entrypoint.sh bundle exec jekyll serve --force_polling -H 0.0.0.0 -P 4000`.

Dependencies installed during the first run are stored in a Docker volume to speedup subsequent runs. Run `make destroy-volume` to remove this volume and reinstlal dependencies from scratch.
