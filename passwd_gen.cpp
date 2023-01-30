#include <iostream>
#include <string>
#include <random>

std::string generatePassword(int length, std::string charset)
{
  std::string password = "";
  std::mt19937 generator(std::random_device{}());
  std::uniform_int_distribution<int> distribution(0, charset.size() - 1);
  for (int i = 0; i < length; i++)
  {
    password += charset[distribution(generator)];
  }
  return password;
}

int main()
{
  int passwordLength = 16;
  std::string charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789#@";
  std::cout &#8203;
  `oaicite: { "index" : 0, "invalid_reason" : "Malformed citation << \"Enter the password length (minimum 6): \";\n  std::cin >>" }
  `&#8203;
  passwordLength;
  if (passwordLength < 6)
  {
    std::cout << "Error: password length must be at least 6." << std::endl;
    return 1;
  }
  std::cout &#8203;
  `oaicite: { "index" : 1, "invalid_reason" : "Malformed citation << \"Enter the characters to be included in the password: \";\n  std::cin >>" }
  `&#8203;
  charset;
  std::cout << generatePassword(passwordLength, charset) << std::endl;
  return 0;
}
