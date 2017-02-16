function setup() {
	createCanvas(400, 400);
}

function draw() {
	house();
}

function house() {
	noStroke();
	background(0, 250, 250);

	//Sun
	fill(255, 255, 0);
	ellipse(20, 20, 200, 200);

	//Rainbow
	noStroke();
	fill(255, 0, 0);
	ellipse(200, 300, 500, 500);
	fill(249, 150, 0);
	ellipse(200, 310, 490, 500);
	fill(255, 255, 0);
	ellipse(200, 320, 480, 500);
	fill(0, 250, 0);
	ellipse(200, 330, 470, 500);
	fill(0, 150, 255);
	ellipse(200, 340, 460, 500);
	fill(100, 0, 205);
	ellipse(200, 350, 450, 500);
	fill(200, 0, 255);
	ellipse(200, 360, 440, 500);
	fill(0, 250, 250);
	ellipse(200, 370, 430, 500);

	//Grass
	fill(0, 255, 0);
	rect(0,300,500,500);

	//House
	fill(255, 204, 0);
	rect(100,200,200,150);

	//Windows
	fill(0, 140, 250);
	rect(130,210,40,40);
	rect(230,210,40,40);
	stroke(255);
	line(149, 210, 149, 250);
	line(150, 210, 150, 250);
	line(151, 210, 151, 250);

	line(130, 229, 170, 229);
	line(130, 230, 170, 230);
	line(130, 231, 170, 231);

	line(249, 210, 249, 250);
	line(250, 210, 250, 250);
	line(251, 210, 251, 250);

	line(230, 229, 270, 229);
	line(230, 230, 270, 230);
	line(230, 231, 270, 231);
	noStroke();

	//Door
	fill(150, 90, 0);
	rect(180,270,40,80);
	fill(150);
	ellipse(188, 310, 8, 8);
	
	//Roof
	fill(150, 10, 0);
	triangle(100, 200, 200, 100, 300, 200);

	//Pipe
	fill(100);
	rect(240, 130, 30, 50);
}