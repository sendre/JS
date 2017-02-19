function setup() {
	createCanvas(400, 400);
}

function draw() {
	house();
}

var sunX = -100;

function house() {
	noStroke();
	background(0, 250, 250);

	//Sun
	fill(255, 255, 0);
	ellipse(sunX, 10, 200);
	sunX += 1;

	if (sunX >= width+100) {
		sunX = -100;
	}

	//Rainbow
	noStroke();
	fill(255, 0, 0, 190);
	ellipse(200, 300, 500, 500);
	fill(249, 150, 0, 190);
	ellipse(200, 310, 490, 500);
	fill(255, 255, 0, 190);
	ellipse(200, 320, 480, 500);
	fill(0, 250, 0, 190);
	ellipse(200, 330, 470, 500);
	fill(0, 150, 255, 190);
	ellipse(200, 340, 460, 500);
	fill(100, 0, 205, 190);
	ellipse(200, 350, 450, 500);
	fill(200, 0, 255, 190);
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

	line(148, 210, 148, 249);
	line(149, 210, 149, 249);
	line(150, 210, 150, 249);
	line(151, 210, 151, 249);

	line(130, 228, 169, 228);
	line(130, 229, 169, 229);
	line(130, 230, 169, 230);
	line(130, 231, 169, 231);

	line(248, 210, 248, 249);
	line(249, 210, 249, 249);
	line(250, 210, 250, 249);
	line(251, 210, 251, 249);

	line(230, 228, 269, 228);
	line(230, 229, 269, 229);
	line(230, 230, 269, 230);
	line(230, 231, 269, 231);
	noStroke();

	//Door
	fill(150, 90, 0);
	rect(180,270,40,80);
	fill(150);
	ellipse(188, 310, 8, 8);
	
	//Roof
	fill(150, 10, 0);
	triangle(80, 200, 200, 100, 320, 200);

	//Pipe
	fill(100);
	rect(250, 130, 30, 50);
}