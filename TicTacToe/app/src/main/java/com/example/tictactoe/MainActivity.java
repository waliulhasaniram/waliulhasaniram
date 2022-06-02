package com.example.tictactoe;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private ImageView i1, i2, i3, i4, i5, i6, i7, i8, i9;
    private Button resetButton;
    private TextView textView;
    private AlertDialog.Builder alertDialogBuilder;
    private String winnerStr;
    ImageView img;
    boolean gameActive = true;

    int activePlayer = 0; //0 = x, 1 = 0

    int[] gameState = {2, 2, 2, 2, 2, 2, 2, 2, 2}; // 0 = x, 1 = 0, 2 = null, empty image view

    int[][] winPosition = {{0,1,2},{3,4,5},{6,7,8},
            {0,3,6},{1,4,7},{2,5,8},
            {0,4,8},{2,4,6}};

    /////////////////////////////////////////////////////////////////// main game code
    public void playerTap(View view) {
        ImageView img = (ImageView) view;
        int TapedImage = Integer.parseInt(img.getTag().toString());

        if(!gameActive)
        {
            return;
        }

        if(gameState[TapedImage] == 2)
        {
            gameState[TapedImage] = activePlayer;
            img.setTranslationY(-1000f);
            if(activePlayer == 0)
            {
                img.setImageResource(R.drawable.cross);
                activePlayer = 1;
                TextView textView =  findViewById(R.id.textView);
                textView.setText("0's turn now");
            }
            else{
                img.setImageResource(R.drawable.zero);
                activePlayer = 0;
                TextView textView =  findViewById(R.id.textView);
                textView.setText("X's turn now");
            }
            img.animate().translationYBy(1000f).setDuration(200);
        }

        for(int[] winPos : winPosition) //////////////////////////////////////// if wins
        {
            if(gameState[winPos[0]] == gameState[winPos[1]] && gameState[winPos[1]] == gameState[winPos[2]]
                    && gameState[winPos[0]] != 2)
            {

                gameActive = false;

                if(gameState[winPos[0]] == 0)
                {
                    winnerStr = "X won the game";
                }
                else
                {
                    winnerStr = "0 won the game";
                }
                TextView textView = (TextView) findViewById(R.id.textView);
                textView.setText(winnerStr);

            }

        }


        boolean emptySquare = false;
        for (int square : gameState) {
            if (square == 2) {
                emptySquare = true;
                break;
            }
        }
        if (!emptySquare && gameActive) {
            // Game is a draw
            gameActive = true;
            String winnerStr;
            winnerStr = "No one won";
            TextView status = findViewById(R.id.textView);
            status.setText(winnerStr);
            return; // if no one wins then nothing will happens
        }

    }

    ////////////////////////////////////////////////////////////////// starting and reset
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ((ImageView) findViewById(R.id.i1)).setImageResource(0);
        ((ImageView) findViewById(R.id.i2)).setImageResource(0);
        ((ImageView) findViewById(R.id.i3)).setImageResource(0);
        ((ImageView) findViewById(R.id.i4)).setImageResource(0);
        ((ImageView) findViewById(R.id.i5)).setImageResource(0);
        ((ImageView) findViewById(R.id.i6)).setImageResource(0);
        ((ImageView) findViewById(R.id.i7)).setImageResource(0);
        ((ImageView) findViewById(R.id.i8)).setImageResource(0);
        ((ImageView) findViewById(R.id.i9)).setImageResource(0);

        textView = (TextView) findViewById(R.id.textView);
        resetButton = (Button) findViewById(R.id.resetButton);

        resetButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                gameActive = true;
                activePlayer = 0;
                for(int j =0; j<gameState.length; j++){
                    gameState[j] = 2; // 2 = null
                }
                ((ImageView) findViewById(R.id.i1)).setImageResource(0);
                ((ImageView) findViewById(R.id.i2)).setImageResource(0);
                ((ImageView) findViewById(R.id.i3)).setImageResource(0);
                ((ImageView) findViewById(R.id.i4)).setImageResource(0);
                ((ImageView) findViewById(R.id.i5)).setImageResource(0);
                ((ImageView) findViewById(R.id.i6)).setImageResource(0);
                ((ImageView) findViewById(R.id.i7)).setImageResource(0);
                ((ImageView) findViewById(R.id.i8)).setImageResource(0);
                ((ImageView) findViewById(R.id.i9)).setImageResource(0);

                textView.setText("game reset! X turn now");

            }
        });
    }

}
