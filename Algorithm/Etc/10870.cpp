#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int pibo(int n) {
	if (n == 2) {
		return 1;
	}
	if (n == 1) {
		return 1;
	}
	if (n == 0) {
		return 0;
	}
	return pibo(n-2)+pibo(n - 1);
}

int main() {
	int n;
	scanf("%d", &n);
	printf("%d\n", pibo(n));
	return 0;
}