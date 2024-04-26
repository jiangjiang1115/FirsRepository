const {
  app,
  BrowserWindow,
  ipcRenderer,
  ipcMain
} = require('electron/main')



const path = require('node:path')
var win
// 绘制窗口
createWindow = () => {
  win = new BrowserWindow({
    // titleBarStyle: 'hidden', //隐藏顶部原生标题及菜单栏样式
    // icon: path.join(__dirname,'./icon.ico'),
    // backgroundColor:'skyblue',
    // transparent: false,  // 当transparent为true会导致win.restore()无效，有向下还原
    // transparent: true,//设置窗体背景透明,圆角窗口，只有最大化，无向下还原
    // frame: false,// 去除顶部操作按钮
    resizable: true,
    icon: 'icon.ico',
    width: 1000,
    height: 680,
    minWidth: 1000,
    minHeight: 680,
    webPreferences: {
      //预加载脚本
      preload: path.join(__dirname, './preload.js'),
      // 让渲染进程支持node
      nodeIntegration: true,
      // enableRemoteModule: true,
      //  contextIsolation开启后 electron 就会认为 require 不可用了
      contextIsolation: false,
    },
    icon:path.join(__dirname,'./public/image/11.png')
  })

  win.loadFile('index.html')

}

// 监听 程序启动
// app.whenReady().then(() => {
//   app.whenReady().then(() => {
//     ipcMain.handle('ping', () => 'pong')
//     createWindow()
//     // //用于macOS，没有打开任何窗口时，打开一个新窗口
//     app.on('activate', () => {
//       if (BrowserWindow.getAllWindows().length === 0) {
//         createWindow()
//       }
//     })
//   })
//   //所有网页关闭时退出应用
//   app.on('window-all-closed', () => {
//     if (process.platform !== 'darwin') {
//       app.quit()
//     }
//   })
// })

//登录窗口最小化
ipcMain.on('window-min', function () {
  win.minimize();
})
//登录窗口最大化
ipcMain.on('window-max', function () {
  if (win.isMaximized()) {
    win.restore();
  } else {
    win.maximize();
  }
})
//关闭窗口
ipcMain.on('window-close', function () {
  win.close();
})

ipcMain.on('renderSend',function(event,result){
  console.log(result);
  event.sender.send=('mainSend','回复'+result);
})


app.whenReady().then(() => {
  // ipcMain.handle('ping', () => 'pong')
  createWindow()
})
// app.on('ready', createWindow)
// app.on('window-all-closed', () => {
//   if (process.platform !== 'darwin') {
//     app.quit()
//   }
// })

