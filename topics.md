Relationships : 
    - ont-to-one         users[1]          profile[1]                    
    - one-to-many        users[1] .        posts[...] . ---> Foreignkey 
    - many-to-many       users[...] .      groups[...]


                        product                 brand
                 1:1       iphone               apple 
                 .:.       iphone               apple
                 1:.       iphone               


                    products                brands
                    iphone                  apple 