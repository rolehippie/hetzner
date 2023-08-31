# hetzner

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/hetzner)
[![General Workflow](https://github.com/rolehippie/hetzner/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/hetzner/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/hetzner/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/hetzner/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/hetzner/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/hetzner/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/hetzner)](https://github.com/rolehippie/hetzner/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.hetzner-blue)](https://galaxy.ansible.com/rolehippie/hetzner)

Ansible role to configure Hetzner repository mirrors.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [hetzner_filename](#hetzner_filename)
  - [hetzner_repos](#hetzner_repos)
  - [hetzner_update_cache](#hetzner_update_cache)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`

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
