using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Script : MonoBehaviour
{
    [SerializeField] private float mSpeed = 1.0f;
    [SerializeField] private float mJump = 1.0f;


    public AudioSource src; 
    [SerializeField] public AudioClip sfx1, sfx2, sfx3;

    private SpriteRenderer sp = null;
    private Rigidbody2D rb = null;



    protected void Start()
    {
        rb = this.GetComponent<Rigidbody2D>();
        sp = this.GetComponent<SpriteRenderer>();
    }


    void Update()
    { 
        Vector3 localDirection;
        localDirection = Vector3.zero;

        if(Input.GetKey(KeyCode.RightArrow))
        {
            localDirection = Vector3.right;
            sp.flipX = false;
          
        }

        else

        if(Input.GetKey(KeyCode.LeftArrow))
        {
            localDirection = Vector3.left;
            sp.flipX = true;
            src.clip = sfx1;
            src.Play();
        }


        Vector3 localWhichVelocity;
        localWhichVelocity = localDirection * mSpeed;
        localWhichVelocity.y = rb.velocity.y;  
        rb.velocity = localWhichVelocity;
        
        
        

    }
    protected void OnCollisionEnter2D(Collision2D localCollision)
    {
        GameObject localOtherObject; 

        localOtherObject = localCollision.gameObject;

        if (localOtherObject.name.StartsWith("Player"))
        {
            this.gameObject.SetActive(false);
        }
    }

}    

