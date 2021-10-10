
def read_chat(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())

	return chat

def covert(chat):
	chat_convert = []
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			chat_convert.append(person + ': ' + line)
	return chat_convert

def write_chat(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')


def main():
	chat = read_chat('對話紀錄相關檔案/對話紀錄1/input.txt')
	chat = covert(chat)
	write_chat('output-test.txt', chat)
	

main()