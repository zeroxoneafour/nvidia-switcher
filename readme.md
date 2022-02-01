# nvidia-swicher
A tool to switch between Nvidia and Nouveau/integrated graphics on Fedora, with LightDM. Works on my systemTM

## building
I provide a simple script that builds the package for you. To build it, run `./build-rpm.sh`. To install it, run `rpm -i ~/rpmbuild/RPMS/noarch/nvidia-switcher-*.rpm` as root.

## installation
1. Follow the instructions on the Fedora wiki [here](https://docs.fedoraproject.org/en-US/quick-docs/how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops/), but ONLY UP UNTIL STEP 7. Do not edit the X11 configuration.
2. Make sure this is the only part of your kernel parameters (usually in `/etc/default/grub`) that concerns the Nouveau driver - `rd.driver.blacklist=nouveau`. Make sure to regenerate grub config (`grub2-mkconfig -o /boot/grub2/grub.cfg`)
3. In the LightDM config (`/etc/lightdm/lightdm.conf`), set `display-setup-script=/etc/lightdm/display_setup.sh`
4. Add something similar to this to `/etc/lightdm/display_setup.sh` - `if [[ -f /etc/lightdm/load-nvidia.sh ]]; then source /etc/lightdm/load-nvidia.sh; fi`
5. [Build and install the RPM](#building)
6. Run nvidia-switcher in a terminal (requires polkit if not run as root)
