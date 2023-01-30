#include <iostream>
#include <string>
#include <random>

std::string generatePassword(int length) {
  std::string password = "";
  std::string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#@";
  std::mt19937 generator(std::random_device{}());
  std::uniform_int_distribution<int> distribution(0, charset.size() - 1);
  for (int i = 0; i < length; i++) {
    password += charset[distribution(generator)];
  }
  return password;
}

int main() {
  int passwordLength = 20;
  std::cout << generatePassword(passwordLength) << std::endl;
  return 0;
}
