class Animation {
    constructor(canvas, imageName, row, col) {
        this.canvas = canvas;
        this.pen = canvas.getContext('2d');
        this.image = new Image();
        this.image.src = imageName;
        this.row = row;
        this.col = col;
        this.indexCol = 0;
        this.indexRow = 0;

        this.x = 0;
        this.y = 0;
    }

    drawImage() {
        let imgWidth = this.image.width / this.col;
        let imgHeight = this.image.height / this.row;
        this.pen.clearRect(this.x, this.y, imgWidth, imgHeight);
        this.pen.drawImage(this.image, this.indexCol * imgWidth, this.indexRow*imgHeight, imgWidth, imgHeight, this.x, this.y, imgWidth, imgHeight);
    }

    updateFrame() {
        this.indexCol < this.col-1 ? this.indexCol++ :this.indexCol = 0;
    }

    setPostion(x,y){
        this.x = x;
        this.y = y;
    }

}


