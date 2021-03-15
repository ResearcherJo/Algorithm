#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int pac(int n) {
	if (n == 0) {
		return 1;
	}
	if (n == 1) {
		return 1;
	}
	return n * pac(n - 1);
}

int main() {
	int n;
	scanf("%d", &n);
	printf("%d", pac(n));
	return 0;
}