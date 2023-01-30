#include <iostream>
#include <string>
#include <random>

std::string generatePassword(int length, std::string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
{
  std::mt19937 generator(std::random_device{}());
  std::uniform_int_distribution<int> distribution(0, charset.length() - 1);

  std::string password;
  for (int i = 0; i < length; i++)
  {
    password += charset[distribution(generator)];
  }

  return password;
}

int main()
{
  int length;
  std::cout<<"Enter the password length (minimum 6): \n";    
  std::cin>>length;

  std::string charset;
  std::cout << "Enter a custom character set (optional): ";
  std::cin.ignore();
  std::getline(std::cin, charset);

  std::cout << "Generated password: " << generatePassword(length, charset.empty() ? "" : charset) << std::endl;

  return 0;
}
