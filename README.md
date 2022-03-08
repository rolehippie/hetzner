# hetzner

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/hetzner) [![Testing Build](https://github.com/rolehippie/hetzner/workflows/testing/badge.svg)](https://github.com/rolehippie/hetzner/actions?query=workflow%3Atesting) [![Readme Build](https://github.com/rolehippie/hetzner/workflows/readme/badge.svg)](https://github.com/rolehippie/hetzner/actions?query=workflow%3Areadme) [![Galaxy Build](https://github.com/rolehippie/hetzner/workflows/galaxy/badge.svg)](https://github.com/rolehippie/hetzner/actions?query=workflow%3Agalaxy) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/hetzner)](https://github.com/rolehippie/hetzner/blob/master/LICENSE)

Ansible role to configure Hetzner repository mirrors.

## Sponsor

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu)

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

- [Default Variables](#default-variables)
  - [hetzner_filename](#hetzner_filename)
  - [hetzner_repos](#hetzner_repos)
  - [hetzner_update_cache](#hetzner_update_cache)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Default Variables

### hetzner_filename

Filename for the repo list

#### Default value

```YAML
hetzner_filename: hetzner-mirror
```

### hetzner_repos

List of Hetzner repo mirrors

#### Default value

```YAML
hetzner_repos:
  - deb http://mirror.hetzner.de/ubuntu/packages {{ ansible_distribution_release }}
    main restricted universe multiverse
  - deb http://mirror.hetzner.de/ubuntu/packages {{ ansible_distribution_release }}-updates
    main restricted universe multiverse
  - deb http://mirror.hetzner.de/ubuntu/packages {{ ansible_distribution_release }}-backports
    main restricted universe multiverse
  - deb http://mirror.hetzner.de/ubuntu/packages {{ ansible_distribution_release }}-security
    main restricted universe multiverse
```

### hetzner_update_cache

Update directly the cache

#### Default value

```YAML
hetzner_update_cache: true
```

## Discovered Tags

**_hetzner_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
