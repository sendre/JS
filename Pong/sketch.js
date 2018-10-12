var skip;
var leftPoints;
var rightPoints;
var rPaddle;
var lPaddle;
var ball;
var angle;

function setup() {
	createCanvas(600, 400);

	rightSkip = 0;
	leftSkip = 0;
	leftPoints = 0;
	rightPoints = 0;
	skip = 6;

	rectMode(CENTER);
	
	rPaddle = {
		h: 50,
		w: 5,
		pos: height/2,
		draw: function() {
			rect(width-10, this.pos, this.w, this.h);
		},
		move: function() {
			//UP_ARROW
			if (keyIsDown(38)) {
				if (this.pos > this.h/2) {
					this.pos -= skip;
				}
			}
			//DOWNN_ARROW
			if (keyIsDown(40)) {
				if (this.pos < height - this.h/2) {
					this.pos += skip;
				}
			}
		}
	};

	lPaddle = {
		h: 50,
		w: 5,
		pos: height/2,
		draw: function() {
			rect(10, this.pos, this.w, this.h);
		},
		move: function() {
			//W
			if (keyIsDown(87)) {
				if (this.pos > this.h/2) {
					this.pos -= skip;
				}
			}
			//S
			if (keyIsDown(83)) {
				if (this.pos < height - this.h/2) {
					this.pos += skip;
				}
			}
		}
	};

	angle = random(-QUARTER_PI, QUARTER_PI);

	ball = {
		diameter: 10,
		x: this.width/2,
		y: this.height/2,
		xSpeed: 5*cos(angle),
		ySpeed: 5*sin(angle),
		draw: function() {
			ellipse(this.x, this.y, this.diameter);
		},
		move: function() {
			this.x += this.xSpeed;
			this.y += this.ySpeed;
		}
	};

	//so that ball will go both ways
	if (random(1) < 0.5) ball.xSpeed *= (-1);
}

function draw() {
	background(0);
	fill(255);
	pointPrint();

	rPaddle.draw();
	lPaddle.draw();
	rPaddle.move();
	lPaddle.move();
	ball.draw();
	ball.move();
	bounce();
}

function pointPrint() {
	textAlign(RIGHT);
	textSize(40);
	fill(255);
	text(rightPoints, width - 60, 75);
	textAlign(LEFT);
	text(leftPoints, 60, 75);
}

function bounce() {
	// IF BALL HITS EITHER OF THE PADDLES
	if (ball.x + ball.diameter/2 > width - 10 - rPaddle.w/2 && 
		ball.y - ball.diameter/2 < rPaddle.pos + rPaddle.h/2 && 
		ball.y + ball.diameter/2 > rPaddle.pos - rPaddle.h/2) {

		if (ball.x < width - 10 - rPaddle.w/2) {
			//double check so the ball cant get in the sides of the paddle
			var dist = ball.y - (rPaddle.pos - rPaddle.h/2);
			angle = map(dist, 0, rPaddle.h, -QUARTER_PI, QUARTER_PI);
			ball.xSpeed = (-5)*cos(angle);
			ball.ySpeed = 5*sin(angle);
		}
	} else if (ball.x - ball.diameter/2 < 10 + lPaddle.w/2 && 
		ball.y - ball.diameter/2 < lPaddle.pos + lPaddle.h/2 && 
		ball.y + ball.diameter/2 > lPaddle.pos - lPaddle.h/2) {
		
		if (ball.x > 10 + lPaddle.w/2) {
			//double check so the ball cant get in the sides of the paddle
			var dist = ball.y - (lPaddle.pos - lPaddle.h/2);
			angle = map(dist, 0, lPaddle.h, -QUARTER_PI, QUARTER_PI);
			ball.xSpeed = 5*cos(angle);
			ball.ySpeed = 5*sin(angle);
		}
	}

	// IF BALL HITS ROOF OR FLOOR
	if (ball.y + ball.diameter/2 > height || 
	 		ball.y - ball.diameter/2 < 0) {
		ball.ySpeed = (-1)*ball.ySpeed;
	}

	// IF BALL MISSES EITHER OF THE PADDLES
	if (miss()) {
		ball.x = width/2;
		ball.y = height/2;
		angle = random(-QUARTER_PI, QUARTER_PI);
		ball.xSpeed = 5*cos(angle);
		ball.ySpeed = 5*sin(angle);
		if (random(1) < 0.5) ball.xSpeed *= (-1);
	}
}

function miss() {
	if (ball.x > width) {
		leftPoints += 1;
		return true;
	} else if (ball.x < 0) {
		rightPoints += 1;
		return true;
	}
	return false;
}
