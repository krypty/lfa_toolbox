# LFA Toolbox

LFA Toolbox is a set of tools to create, view and play with fuzzy systems. Ideal for students to play with fuzzy systems.

## Installation

The detailed install instructions can be found here [docs/INSTALL.md](docs/INSTALL.md) but
you basically need to do:

`pip install lfa-toolbox`

## Features

* Singleton and Mamdani fuzzy system types
* Commonly used membership functions (Trap. MF, Triangle MF, Free shape MF,..)
* Multiple consequents
* Default rule
* NOT conditions
* Viewers (membership function viewer, linguistic variable viewer,...)

## Examples

### Membership functions

**TODO** hand-crafted mf + triangular mf + linPWMF + screenshot viewer

### Linguistic variable

**TODO** hand-crafted lv + three points lv + p points lv + screenshot viewer

### Fuzzy System

#### Mamdani

#### Singleton

### Surface viewer

**TODO** example + viewer

### Others examples

A list of examples can be found here [lfa_toolbox/examples](lfa_toolbox/examples).

Here is a output example of the resort problem (available in the examples folder).

## Integration with Trefle

[Trefle](https://github.com/krypty/trefle) is a scikit-learn compatible
estimator implementing the FuzzyCoCo algorithm that uses a cooperative
coevolution algorithm to find and build interpretable fuzzy systems.

See [Trefle's Github](https://github.com/krypty/trefle) to learn how to
install it.

Basically after running Trefle you can save the best fuzzy system and fine tune
it with LFA Toolbox. For example you can change the values of the membership
functions or remove a too specific fuzzy rule.

See [/lfa_toolbox/examples/import_a_trefle_fuzzy_system.py](/lfa_toolbox/examples/import_a_trefle_fuzzy_system.py) example.

## Deployment and Tests

Both documentations are available in the `docs` folder.


## Credits

* Gary Marigliano (developper)
* Carlos Andrés PEÑA REYES (project manager)
* [CI4CB Team](http://iict-space.heig-vd.ch/cpn/)
