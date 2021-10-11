
def read_chat(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())

	return chat


def covert(chat):
	allen_count_number = 0
	allen_count_img = 0
	allen_count_sticker = 0
	viki_count_number = 0
	viki_count_img = 0
	viki_count_sticker = 0
	for line in chat:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_count_img += 1
			elif s[2] == '貼圖':
				allen_count_sticker += 1
			else:
				for m in s[2:]:
					allen_count_number += len(m)
		elif name == 'Viki':
			if s[2] == '圖片':
				viki_count_img += 1
			elif s[2] == '貼圖':
				viki_count_sticker += 1
			else:
				for m in s[2:]:
					viki_count_number += len(m)
	print('Allen用了', allen_count_number, '個字')
	print('Allen用了', allen_count_img, '張圖')
	print('Allen用了', allen_count_sticker, '張貼圖')
	print('Viki用了', viki_count_number, '個字')
	print('Viki用了', viki_count_img, '張圖')
	print('Viki用了', viki_count_sticker, '張貼圖')


def write_chat(filename, chat):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chat:
			f.write(line + '\n')


def main():
	chat = read_chat('對話紀錄相關檔案/對話紀錄2/LINE-Viki.txt')
	chat = covert(chat)
	#write_chat('output-line.txt', chat)
	

main()