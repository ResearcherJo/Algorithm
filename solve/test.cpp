#include <iostream>
#include <string>

int main()
{
	// 변수 선언
	std::string input;

	// 입력 받기
	std::cout << "문자열을 입력하세요: ";
	std::getline(std::cin, input);

	// 출력하기
	std::cout << "입력한 문자열: " << input << std::endl;

	return 0;
}
