# Set bot pairs here

pairs = [
    [
        r'my name is (.*)',
        [
            'Hello %1, how are you today?',
        ]
    ],
    [
        r'what is your name ?',
        ['My name is Chatty and I\'m a chatbot ?']
    ],
    [
        r'how are you ?',
        ['I\'m doing good! How about You ?']
    ],
    [
        r'sorry (.*)',
        ['Its alright', 'Its OK, never mind']
    ],
    [
        r'i\'m (.*) doing good',
        ['Nice to hear that', 'Alright :)']
    ],
    [
        r'hi|hey|hello',
        [
            'Hello',
            'Hey there'
        ]
    ],
    [
        r'(.*) age?',
        [
            'I\'m a computer program dude. Seriously you are asking me this?',
        ]
    ],
    [
        r'what (.*) want ?',
        [
            'Make me an offer I can\'t refuse.',
        ]   
    ],
    [
        r'(.*) created ?',
        [
            'Someone created me using Python\'s NLTK library.',
            'Top secret.'
        ]
    ],
    [
        r'(.*) (location|city) ?',
        [
            'Dokuz Eylül University, Izmir.',
        ]
    ],
    [
        r'how is weather in (.*)?',
        [
            'Weather in %1 is awesome, like always.',
            'Too hot man here in %1.',
            'Too cold man here in %1.',
            'Never even heard about %1.',
        ]
    ],
    [
        r'i work in (.*)?',
        [
            '%1 is an amazing company. But they are in huge loss these days.',
        ]
    ],

    [
        r'(.*)raining in (.*)',
        [
            'No rain since last week here in %2.',
            'Damn its raining too much here in %2.',
        ]
    ],
    [
        r'how (.*) health(.*)',
        [
            'I\'m a computer program, so I\'m always healthy but thanks.',
        ]
    ],
    [
        r'(.*) (sports|game) ?',
        [
            'I\'m a big fan of football.',
        ]
    ],
    [
        r'who (.*) sportsperson ?',
        [
            'Messi',
            'Ronaldo',
            'Rooney'
        ]

    ],
    [
        r'who (.*) (moviestar|actor)?',
        [
            'Brad Pitt'
        ]

    ],
    [
        r'bye',
        [
            'Take care. See you soon. :) ',
            'It was nice talking to you. See you soon. :)'
        ]

    ],
    [
        r'(.*)',  # default response if no patterns from above is found
        [
            'Sorry I don\'t understand you. :(',
            'I am not programmed to understand what you just said.'
            'Are you sure you are speaking English?'
        ],
    ]
]
