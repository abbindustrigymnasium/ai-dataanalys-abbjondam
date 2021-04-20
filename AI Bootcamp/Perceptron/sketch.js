let points = [];
let trainingindex=0;
let p;
let iteration=0;
let autoiterations=0;
let right=0;
let wrong=0;
    //  let points= new Point[100];
    function setup() {
      createCanvas(700, 700);
        p = new Perceptron(3);
    for (let i = 0; i < 100; i++) {
        points.push(new Point());

    }
    }
    function draw() {
        background(255);
        stroke(0);
// line(0,height,width,0);

//Draw the line
let p1= new Point(-1,f(-1));
let p2= new Point(1,f(1));
line(p1.pixelX(),p1.pixelY(),p2.pixelX(),p2.pixelY())
//Draw the Gueesd line
let p3= new Point(-1,p.guessY(-1));
let p4= new Point(1,p.guessY(1));
line(p3.pixelX(),p3.pixelY(),p4.pixelX(),p4.pixelY())
        points.forEach(point => {
            point.show();
        });
        right=0;
        wrong=0;
        points.forEach(point => {
            let inputs=[point.x,point.y,point.bias];
            // p.train(inputs,point.label);

            let guess= p.guess(inputs);
// console.log("Guess: "+guess+"Real: "+ point.label)
            if (guess== point.label) {
                fill(0,255,0);
                right++;
            }
            else{
                fill(255,0,0);
            wrong++;
            }
             noStroke();
            ellipse(point.pixelX(),point.pixelY(),12,12);
        });

//Avkommentera det här för att köra den automatiskt.
if (right!=points.length) {

        let training = points[trainingindex];
            let inputs=[training.x,training.y,training.bias];
        let target = training.label;
        p.train(inputs,target)
        trainingindex++;
        autoiterations++;
        if (autoiterations % 50==0) {
            
        //document.getElementById("logger").innerText+="\n Autoiteration:"+autoiterations+"Rights:"+right+"   Wrongs:"+wrong;
        }
        if (trainingindex==points.length) {
            trainingindex=0;
        }
}

            //Stänger av loopen
        //   noLoop();
    }

   function mousePressed(){
        document.getElementById("logger").innerText+="Rights:"+right+"   Wrongs:"+wrong;
        iteration++;
        document.getElementById("iteration").innerText="Iteration:"+iteration;
    points.forEach(point => {
            let inputs=[point.x,point.y,point.bias];
            p.train(inputs,point.label);
        });
   }

function f(x) {
    //y= mx+b
    return -0.3*x-0.2;
}

class Point {

 constructor(x_,y_){
        this.label = "";
        this.bias= 1;
        if(!arguments.length) {
            this.y= random(-1,1);
        this.x= random(-1,1);
        }
        else
{
    this.x= x_;
        this.y= y_;
}

    let lineY= f(this.x);
        if (this.y>lineY) {
            this.label=1
        }
        else
        {
            this.label=-1
        }
    }

    pixelX()
    {
        return map(this.x,-1,1,0,width);
    }
    pixelY()
    {
        return map(this.y,-1,1,height,0)
    }
    show(){
        stroke(0);
        if (this.label==1) {
            fill(255);
        }
        else
        {
            fill(0);
        }
        let px= this.pixelX();
        let py= this.pixelY();

        ellipse(px,py,16,16);
    }
}

    class Perceptron {
      constructor(n) {
        this.weights = new Array(n);
        this.learningrate=0.011;
        for (let i = 0; i < this.weights.length; i++) {
          this.weights[i] = random(-1, 1);
        }
        console.log(this.weights);
      }

      guess(inputs) {
        let sum = 0;
        for (let i = 0; i < this.weights.length; i++) {
          sum += inputs[i] * this.weights[i];
        }
        let output = this.sign(sum);

        return output;
      }

      guessY(x)
      {
          let m = this.weights[1] /this.weights[0];
          let b= this.weights[2];
          let w0= this.weights[0];
          let w1 = this.weights[1];
          let w2 = this.weights[2];
          return -(w2/w1) - (w0/w1) * x;
      }
      //Activation function
      sign(n) {
        if (n > 0) {
          return 1;
        } else {
          return -1;
        }
      }

      train(inputs, target)
      {
          let guess= this.guess(inputs);
          let error= target - guess;
          for (let i = 0; i < this.weights.length; i++) {
            this.weights[i] +=  error * inputs[i]* this.learningrate;

          }
      }

    }