install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build --out-dir ./dist

package-install:
	uv tool install ./dist/babababa-0.1.0-py3-none-any.whl

.PHONY: install VD-games build package-install

lint:
	uv run ruff check VD_games
