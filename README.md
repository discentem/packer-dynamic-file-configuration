## packer-dynamic-generation-tools

Experimenting with dynamically generating files needed for building images with packer, particularly for Windows images.

So far `render_autoattend.py` is the most far along. It converts YML into a dictionary and then templates a jinja template file to produce the `autounattend.xml`.
