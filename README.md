# hetzner

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/hetzner/status.svg)](https://cloud.drone.io/rolehippie/hetzner)

Ansible role to configure hetzner

## Table of content

* [Default Variables](#default-variables)
  * [hetzner_filename](#hetzner_filename)
  * [hetzner_repos](#hetzner_repos)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

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

## Dependencies

None.

## License

Apache-2.0

## Author

Thomas Boerger
