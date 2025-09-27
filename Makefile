install:
	uv sync

brain-games:
	uv run brain-games

clean-dist:
	rm -rf dist/

build: clean-dist
	uv build

package-install:
	uv tool install --force dist/*.whl
