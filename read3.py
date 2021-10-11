
def open_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def arrange_chat(lines):
	s = []
	time = []
	name =[]
	for line in lines:
		s = line.split(' ')
		time = s[0][:5]
		name = s[0][5:]
		print(name, ':', s[1])


def main():
	lines = open_file('對話紀錄相關檔案/對話紀錄3/3.txt')
	arrange_chat(lines)

main()