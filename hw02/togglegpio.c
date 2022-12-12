#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

// The memory address of the GPIO registers on the BeagleBone
#define GPIO0_START_ADDR 0x44e07000
#define GPIO0_END_ADDR   0x44e09000
#define GPIO0_SIZE (GPIO0_END_ADDR - GPIO0_START_ADDR)

#define GPIO_OE 0x134
#define GPIO_DATAIN 0x138
#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190

// The pin number to toggle (using GPIO1_17)
#define PIN_NUM (1*32 + 17)

int main(int argc, char* argv[]) {
  int fd = open("/dev/mem", O_RDWR);
  if (fd == -1) {
    perror("Unable to open /dev/mem");
    return 1;
  }

  void *gpio_map = mmap(NULL, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);
  if (gpio_map == MAP_FAILED) {
    perror("Unable to map GPIO registers");
    return 1;
  }

  // Enable the GPIO pin for output
  volatile unsigned int *gpio_oe_addr = gpio_map + GPIO_OE;
  volatile unsigned int *gpio_setdataout_addr = gpio_map + GPIO_SETDATAOUT;
  volatile unsigned int *gpio_cleardataout_addr = gpio_map + GPIO_CLEARDATAOUT;

  // Set the specified pin as an output
  *gpio_oe_addr &= ~(1 << PIN_NUM);

  // Toggle the pin as fast as possible
  while (1) {
    *gpio_setdataout_addr = 1 << PIN_NUM;
    *gpio_cleardataout_addr = 1 << PIN_NUM;
  }

  return 0;
}
