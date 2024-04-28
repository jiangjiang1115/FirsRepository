var ipcRenderer = require('electron').ipcRenderer;

var http = require('https');

var fs = require('fs');
var path = require('path');

var collectionSong = 11;

// 窗口控制：最大化、最小化、关闭
document.getElementById('maxbt').addEventListener('click', () => {
   ipcRenderer.send('window-max');
})
document.getElementById('minbt').addEventListener('click', () => {
   ipcRenderer.send('window-min');

})
document.getElementById('closebt').addEventListener('click', () => {
   ipcRenderer.send('window-close');
})

// 搜索框：回车搜索
function onkeypressfunction() {
   if (event.keyCode === 13) {
      //判断：如果（if）按的是回车键（回车键的keyCode值是13）
      search();
   }
}

// 切换到搜索页面
function search() {
   var iframes = document.getElementById("iframes");
   iframes.setAttribute('src', "./searchResult.html");

   // 侧边栏
   // 改背景色
   var history = document.getElementById("history");
   history.style.backgroundColor = 'rgb(240, 243, 246)';
   history.style.color = 'rgb(107, 114, 126)';
   var collection = document.getElementById("collection");
   collection.style.backgroundColor = 'rgb(240, 243, 246)';
   collection.style.color = 'rgb(107, 114, 126)';
   // 改图标
   var navImg1 = document.getElementsByClassName("navImg")[0];
   navImg1.src = "./public/image/history.png";
   var navImg2 = document.getElementsByClassName("navImg")[1];
   navImg2.src = "./public/image/collection.png";

   // 获取输入框的值
   var searchValue = document.getElementById("searchValue");
   console.log('点击了发送函数！', searchValue.value);
   // 点击传值
   result = "https://s.music.163.com/search/get?s=[" + searchValue.value + "]&type=1&limit=";
   console.log(result);
   var songs = '';
   // 获取歌曲id
   http.get(result, function (req, res) {
      var SongId = '';

      console.log('statusCode:', req.statusCode);
      console.log("已经发送请求");
      //用于监听data函数，是否有读取新数据
      req.on('data', function (data) {
         console.log("\n\n\n");
         console.log("获取数据")
         SongId += data;
         // console.log(SongId);
         // 处理并返回前端页面
      });
      //监听是否读取完毕
      req.on('end', function () {
         console.log("请求结束");
         // 字符串转字典
         SongId = eval('(' + SongId + ')');
         // console.log(SongId);
         songs = SongId['result']['songs'];
         // console.log(typeof (songs[0]))
         addSongResult(songs);
      });
   })
}

// 收藏歌曲
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
      loadCollect(loadCollection.innerHTML)
   }
}
function loadCollect(collectionSong) {
   var loadCollection = window.parent.document.getElementById("loadCollection")
   loadCollection.innerHTML = collectionSong
}


// 双击切换歌曲
function changeSong(songs) {
   // songs[i]["id"]},'${songs[i]["album"]["picUrl"]
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
   changeSong.src = "https://music.163.com/song/media/outer/url?id=" + songs["id"] + ".mp3"
   audio.load()
   audio.play()

   audio.oncanplay = function () {
      console.log("音乐时长", audio.duration);//音乐总时长
      //处理时长
      var time = audio.duration;
      //分钟
      var minute = time / 60;
      var minutes = parseInt(minute);
      if (minutes < 10) {
         minutes = "0" + minutes;
      }
      //秒
      var second = time % 60;
      var seconds = Math.round(second);
      if (seconds < 10) {
         seconds = "0" + seconds;
      }
      console.log('处理音乐时长', minutes + "：" + seconds);

   }
   songs = encodeURIComponent(JSON.stringify(songs))
   addHistory(songs)

}


// 将元素写入试听
function addHistory(songs) {
   var songs = JSON.parse(decodeURIComponent(songs));
   songsInfo = encodeURIComponent(JSON.stringify(songs))
   var loadHistory = window.parent.document.getElementById("loadHistory")
   var loadCollection = window.parent.document.getElementById("loadCollection");
   var addSong = ` <div class="songContainer" ondblClick="changeSong('${songsInfo}')">
                        <span>${songs["name"]}</span>
                        <span>${songs['artists'][0]['name']}</span>
                           <span>${songs['album']['name']}</span>
                        <span><img onClick="addCollection('${songsInfo}')" id="${songs["id"]}"  src="./public/image/collection.png" alt=""></span>
                        </div>`
   collected = loadCollection.innerHTML.split("</div>");
   // console.log(collected)
   // 判断是否已收藏
   for (i = 0; i <= collected.length; i++) {

      if (collected[i] && collected[i].match(songs["id"])) {
         console.log(collected[i])
         console.log(songs["id"], "-->这个歌曲被收藏了")
         addSong = ` <div class="songContainer" ondblClick="changeSong('${songsInfo}')">
                              <span>${songs["name"]}</span>
                              <span>${songs['artists'][0]['name']}</span>
                              <span>${songs['album']['name']}</span>
                              <span><img onClick="addCollection('${songsInfo}')" id="${songs["id"]}"  src="./public/image/star.png" alt=""></span>
                        </div>`

      }
   }
   loadHistory.innerHTML += addSong
}

// 搜索结果展示
function addSongResult(songs) {
   var searchValue = document.getElementById("searchValue");
   // 获取嵌套页面的doc,获取search页面的标签，写入
   var idoc = iframes.contentWindow.document;
   var searchSpan = idoc.getElementById("search");
   // console.log(searchSpan);
   // 传递搜索关键词
   searchSpan.innerText = searchValue.value;

   // 处理数据，循环
   console.log(typeof (songs))
   var resultSong = idoc.getElementById("resultSong");
   var loadCollection = document.getElementById("loadCollection");
   collected = loadCollection.innerHTML.split("</div>");
   var addSong;
   // console.log(collected);

   for (var i in songs) {
      // 将获取的歌曲信息编码，用于函数传值
      songsInfo = encodeURIComponent(JSON.stringify(songs[i]))
      // console.log(songsInfo)
      // console.log(JSON.parse(decodeURIComponent(songsInfo)))
      addSong = ` <div class="songContainer" ondblClick="changeSong('${songsInfo}')">
                              <span>${songs[i]["name"]}</span>
                              <span>${songs[i]['artists'][0]['name']}</span>
                              <span>${songs[i]['album']['name']}</span>
                              <span><img onClick="addCollection('${songsInfo}')" id="${songs[i]["id"]}"  src="./public/image/collection.png" alt=""></span>
                        </div>`
      getID = songs[i]["id"]

      //判断是否已收藏
      for (j = 0; j <= collected.length; j++) {
         // 拆分的内容，找歌曲id
         if (collected[j] && collected[j].match(getID)) {
            // console.log(collected[i])
            console.log(getID, "-->这个歌曲被收藏了")
            addSong = ` <div class="songContainer" ondblClick="changeSong('${songsInfo}')">
                              <span>${songs[i]["name"]}</span>
                              <span>${songs[i]['artists'][0]['name']}</span>
                              <span>${songs[i]['album']['name']}</span>
                              <span><img onClick="addCollection('${songsInfo}')" id="${songs[i]["id"]}"  src="./public/image/star.png" alt=""></span>
                        </div>`

         }
      }
      resultSong.innerHTML += addSong
   }
}

//切换最近播放界面
function toHistory() {
   var iframes = document.getElementById("iframes");
   iframes.src = "./history.html";

   // 侧边栏
   // 改背景色
   var history = document.getElementById("history");
   history.style.backgroundColor = 'rgb(45, 196, 146)';
   history.style.color = '#fff';
   var collection = document.getElementById("collection");
   collection.style.backgroundColor = 'rgb(240, 243, 246)';
   collection.style.color = 'rgb(107, 114, 126)';
   // 改图标
   var navImg1 = document.getElementsByClassName("navImg")[0];
   navImg1.src = "./public/image/history1.png";
   var navImg2 = document.getElementsByClassName("navImg")[1];
   navImg2.src = "./public/image/collection.png";
}
// 切换到收藏界面
function toCollection() {
   var iframes = document.getElementById("iframes");
   iframes.src = "./collection.html";

   // 侧边栏
   // 改背景色
   var history = document.getElementById("history");
   history.style.backgroundColor = 'rgb(240, 243, 246)';
   history.style.color = 'rgb(107, 114, 126)';
   var collection = document.getElementById("collection");
   collection.style.backgroundColor = 'rgb(45, 196, 146)';
   collection.style.color = '#fff';
   // 改图标
   var navImg1 = document.getElementsByClassName("navImg")[0];
   navImg1.src = "./public/image/history.png";
   var navImg2 = document.getElementsByClassName("navImg")[1];
   navImg2.src = "./public/image/collection1.png";


}

// 歌曲播放暂停，audio控制
function SongSwitch() {
   startPic = document.getElementById("start");
   audio = document.getElementById("audio");
   picName = startPic.src.split("/").pop();
   if (picName == "stop.png") {
      startPic.src = "./public/image/start.png";
      audio.play();
   } else {
      startPic.src = "./public/image/stop.png";
      audio.pause();
   }
}


// 获取当前页面元素作为歌单，双击播放调用，向前向后切换歌曲（正序逆序）
function SongsList() {
   // 歌单列表滑出
   songsList = document.getElementById('songsList');
   if (songsList.style.left == '-170px') {
      songsList.style.left = '130px'
   } else {
      songsList.style.left = '-170px'
   }

   resultSong = document.getElementById('resultSong');

   //获取子页面元素  
   var iframes = document.getElementById("iframes");
   var idoc = iframes.contentWindow.document;
   // console.log(iframes.src.split('/').pop())
   if (iframes.src.split('/').pop() == 'collection.html') {
      load = document.getElementById('loadCollection')
      resultSong.innerHTML = load.innerHTML
   } else {
      load = document.getElementById('loadHistory')
      resultSong.innerHTML = load.innerHTML
   }


   // var searchValue = document.getElementById("searchValue");
   // // 获取嵌套页面的doc,获取search页面的标签，写入

   // var searchSpan = idoc.getElementById("search");
}