// 收藏 & 取消收藏
function addCollection(songs) {
    var loadCollection = window.parent.document.getElementById("loadCollection")
    var songs = JSON.parse(decodeURIComponent(songs));
    var star = event.currentTarget;
    // console.log(star)
    starIcon = star.src.split("/").pop()
    // console.log(starIcon)
    songsInfo = encodeURIComponent(JSON.stringify(songs))
    if (starIcon == "star.png") {
       // 删除收藏歌曲
       star.src = "./public/image/collection.png";
       // 获取字符串里的歌曲id,删除有歌曲id的部分
       collected = loadCollection.innerHTML.split("</div>")
       // console.log(loadCollection.innerHTML)
       // console.log(collected)
       for (i = 0; i <= collected.length; i++) {
          if (collected[i] && collected[i].match(songs["id"])) {
             collected[i] = ''
             console.log('getgetget')
             // console.log(collected[i])
          } else if (collected[i]) {
             collected[i] += "</div>"
             // console.log(collected[i])
          }
       }
       loadCollection.innerHTML = collected.join("")
       var iframes = window.parent.document.getElementById('iframes')
       if (iframes.src.split('/').pop() == 'collection.html') {
          iframes.contentWindow.location.reload(true);
       }
 
    } else {
       // 添加收藏
 
       star.src = "./public/image/star.png";
       var addSong = ` <div class="songContainer" ondblClick="changeSong('${songsInfo}')">
                    <span>${songs["name"]}</span>
                    <span>${songs['artists'][0]['name']}</span>
                    <span>${songs['album']['name']}</span>
                    <span><img onClick="addCollection('${songsInfo}')" id="${songs["id"]}"  src="./public/image/star.png" alt=""></span>
                 </div>`
       loadCollection.innerHTML += addSong
    }
 
 }

 // 双击切换歌曲
function changeSong(songs) {
    var songs = JSON.parse(decodeURIComponent(songs));
    // console.log(songs)
    console.log("触发双击事件")
    // 获取iframe父页面元素
    var audio = window.parent.document.getElementById("audio");
    var startPic = window.parent.document.getElementById("start");
    startPic.src = "./public/image/start.png";
    var songPicEl = window.parent.document.getElementById("songPic");
    // console.log(songPicEl)
    songPicEl.src = songs["album"]["picUrl"]
 
    var changeSong = window.parent.document.getElementById("changeSong");
    changeSong.className = songs["id"] + "/" + songs['artists'][0]['name'] + "/" + songs["album"]["picUrl"]
    changeSong.src = "https://music.163.com/song/media/outer/url?id=" + songs["id"] + ".mp3"
 
    var songName = window.parent.document.getElementById("songName");
    var songArtists = window.parent.document.getElementById("songArtists");
    songName.innerText = songs["name"]
    songArtists.innerText = songs['artists'][0]['name']
 
    audio.load()
    audio.play()
 
    // audio.oncanplay = function () {
    //    console.log("音乐时长", audio.duration);//音乐总时长
    //    //处理时长
    //    var time = audio.duration;
    //    //分钟
    //    var minute = time / 60;
    //    var minutes = parseInt(minute);
    //    if (minutes < 10) {
    //       minutes = "0" + minutes;
    //    }
    //    //秒
    //    var second = time % 60;
    //    var seconds = Math.round(second);
    //    if (seconds < 10) {
    //       seconds = "0" + seconds;
    //    }
    //    console.log('处理音乐时长', minutes + "：" + seconds);
 
    // }
    // songs = encodeURIComponent(JSON.stringify(songs))
    // addHistory(songs)
 
 }

 