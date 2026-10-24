# horizon-theme-daemon

A modern theme for the OpenStack dashboard inspired by [Beastie](https://en.wikipedia.org/wiki/BSD_Daemon).

## Features

- light and dark variants
- sheets instead of modals for creating and editing resources
- refreshed project and admin overview pages

## Configuration

Install the Python package somewhere Horizon can import it.

Add the theme to `local_settings.py`:

```python
from daemon_theme import THEMES

AVAILABLE_THEMES = THEMES
DEFAULT_THEME = "daemon"
```

`THEMES` holds the light `daemon` and the dark `daemon-dark` theme.

The header and the login card show `SITE_BRANDING` beside the mark.

Then collect and compress the static files and restart Horizon:

```sh
django-admin collectstatic --noinput
django-admin compress --force
```

## Licences

Inter is licensed under the SIL Open Font License 1.1, see `src/daemon_theme/theme/static/fonts/Inter-LICENSE.txt`.

The rest of the theme is Apache 2.0.
