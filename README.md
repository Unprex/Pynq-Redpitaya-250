# PYNQ for Redpitaya-250-12

---

ℹ️ Forked from [PYNQ for Redpitaya-125-14](https://github.com/dspsandbox/Pynq-Redpitaya-125) by [Pau Gómez](https://github.com/dspsandbox).

---

## Information and links

* [Pynq-Redpitaya-250-12-3.0.1.img](https://cloud.univ-grenoble-alpes.fr/s/gTwcae78kWszprC)
* [Instructions on writing the SD card image](https://pynq.readthedocs.io/en/v2.6.1/appendix.html#writing-the-sd-card-image)
* [Getting started with PYNQ](https://pynq.readthedocs.io/en/v2.0/getting_started.html)
* [Quick Steps to Modify Device Tree](https://gist.github.com/yunqu/827862e580a5f9b069eccdfcdcf70398)
* [image.ub and zImage](https://cloud.univ-grenoble-alpes.fr/s/XnZNMa4cXNrfHis)

## Build process

### Get the environment ready

We follow the steps outlined under [PYNQ SD card](https://pynq.readthedocs.io/en/v3.0.0/pynq_sd_card.html):

* Install a virtual machine running Ubuntu **18_04_4 LTS** with more than 150 GB of storage space. Do not update Ubuntu since this will roll the version and make it *officially* incompatible with the Xilinx tools below (for this build we used **Ubuntu 18.04.6 LTS** with security updates).

* Clone the PYNQ repository (for this build we used **v3.0.1**):
```bash
git clone https://github.com/Xilinx/PYNQ
```

* Install dependencies using the following script.
```bash
source <PYNQ repository>/sdbuild/scripts/setup_host.sh
```

* Install the Xilinx tools (for this build we used **v2022.1**):
   * Vitis (which includes Vivado)
   * Petalinux
   * Go for lunch! This will take a few hours...

* Download the prebuilt board-agnostic (PYNQ rootfs arm v3.0.1) image from [Pynq Development Boards ](http://www.pynq.io/board.html/) and unzip it.
* Download the PYNQ distribution tarball (pynq-3.0.1.tar.gz) from the [PYNQ release repository](https://github.com/Xilinx/PYNQ/releases). You will find the distribution tarball under a drop-down called *Assets*.
* Place both files into *<PYNQ repository>/sdbuild/prebuilt/*
* Rename files to *pynq_rootfs.arm.tar.gz* and *pynq_sdist.tar.gz*

### Prepare build

* Clone this repository:
```bash
git clone https://github.com/Unprex/Pynq-Redpitaya-250
```

* Make sure the scripts in the Pynq/boards folder are executable:
```bash
sudo chmod -R 777 Pynq-Redpitaya-250/Pynq/boards
```

### Build PYNQ

* Open a terminal and run the settings files for Vitis and Petalinux:
```bash
source <path-to-vitis>/2022.1/settings64.sh
source <path-to-petalinux>/2022.1/settings.sh
```

* Navigate to
```bash
cd <PYNQ repository>/sdbuild
```

* Run the makefile (your password will be required a couple of times)
```bash
make BOARDS=Pynq-Redpitaya-250-12 BOARDDIR=/path/to/Pynq/boards
```

* The generated PYNQ image will be located within *\<PYNQ repository\>/sdbuild/output/Pynq-Redpitaya-250-12-3.0.1.img*

* *image.its* and *zImage* will be located in *\<PYNQ repository\>/sdbuild/build/RP25012/*
