# pyloss

Loss classes for use on Image-based Machine Learning.

[![Build Tests](https://img.shields.io/github/workflow/status/rlaPHOENiX/pyloss/Version%20test?label=Python%203.5%2B%20builds)](https://github.com/rlaPHOENiX/pyloss/actions?query=workflow%3A%22Version+test%22)
[![License](https://img.shields.io/github/license/rlaPHOENiX/pyloss?style=flat)](https://github.com/rlaPHOENiX/pyloss/blob/master/LICENSE)
[![DeepSource](https://deepsource.io/gh/rlaPHOENiX/pyloss.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/rlaPHOENiX/pyloss/?ref=repository-badge)
[![Issues](https://img.shields.io/github/issues/rlaPHOENiX/pyloss?style=flat)](https://github.com/rlaPHOENiX/pyloss/issues)
[![PR's Accepted](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](https://makeapullrequest.com)

* * *

## Not yet ready for prime time use

This project is still under very early stages, and I don't recommend using it for now.

* * *

## Quick Installation

    pip install pyloss

* * *

## Building

This project is firmly requiring the use of Python PIP with [PEP 517][pep517] support. This means you need `pip >= 19`
[(ref)][pip19].

Considering version `19.0` released on the 22nd of January 2019, it isn't much of an ask in my opinion, when you end up
with an overall much smoother build experience.

Once you have pip with PEP 517 support, it's as simple as 3 calls:

    pip install build
    git clone https://github.com/rlaPHOENiX/pyloss && cd pyloss
    python -m build

To install the built project, install the .whl file available in /dist, e.g. `pip install dist/*.whl`

If you want to simply install from the source, instead of `python -m build` run `pip install .`

[pep517]: https://www.python.org/dev/peps/pep-0517

[pip19]: https://pip.pypa.io/en/stable/news/#id415

* * *

## License

This project is released under the MIT license.
Please read and agree to the license before use, it can be found in the [LICENSE](LICENSE) file.
