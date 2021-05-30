alert('oke broh selamat datang');
var lagi = (confirm('mau main?'));


while(lagi === true)
{
var nama = prompt('masukin nama dulu lah..');
alert('oke '+nama+' udah siap?');
alert('ini pertanyaanya, Berapa jumlah pulau di indonesia?');


var jawab = prompt('jawab:');

alert ('bentar lagi ngitung')

if(jawab === '17,500') {
	alert('oke jawabannya bener:)');
} else {
	alert('selamat jawaban anda "SALAH"');
}

lagi = confirm('main lagi?');
};
