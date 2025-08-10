from blog.models import Post
from django.core.management.base import BaseCommand
from typing import Any




class Command(BaseCommand):
    help = "data uploded successfully"

    def handle(self, *args: Any, **options: Any):

        Post.objects.all().delete()

        titles = [
            "British Shorthair",
            "Siamese",
            "Doll Face Persian",
            "Bengal Cat",
            "Exotic Shorthair",
            "Sphynx",
            "Birman",
            "Oriental Shorthair",
            "Persian cat",
        ]
        contents = [
            "The British Shorthair is one of the oldest and most cherished cat breeds, renowned for its robust build, plush double coat, and iconic round face. Often seen in a signature “British Blue” coat with copper-orange eyes, this breed comes in a variety of other colors and patterns as well. These cats have a calm, easygoing temperament and are known to be incredibly loyal but not overly demanding. They enjoy being near their humans but aren’t particularly clingy, making them perfect for people who want a companionable pet without the constant need for attention.",
            "The Siamese cat is a striking and elegant breed known for its piercing blue almond-shaped eyes, sleek body, and signature pointed color pattern, which features a pale body with darker accents on the ears, face, paws, and tail. Originating in Thailand (formerly Siam), this breed is one of the oldest and most recognizable cat breeds in the world, often celebrated for its regal looks and distinct personality. Siamese cats are exceptionally vocal and social; they love interacting with humans and will often follow their owners from room to room, 'talking' with a unique, loud meow known as a 'meezer'. ",
            "The Doll Face Persian, also called the Traditional Persian, offers a more natural and classic look compared to the flat-faced 'Peke' Persian that many people associate with the breed today. This variety features a sweet, gently rounded face with a normal-length nose, giving them a charming and expressive appearance that many find more appealing and healthier than their modern counterparts. Their long, flowing coats are incredibly luxurious and come in an array of stunning colors and patterns, but they do require consistent grooming—daily brushing is often necessary to prevent tangles and mats.",
            "The Bengal cat is a stunning breed that combines the wild beauty of a leopard with the affectionate personality of a domestic cat. Known for its striking spotted or marbled coat, which often has a glittering effect, the Bengal was developed by crossing domestic cats with the Asian leopard cat. This gives them an exotic, jungle-like appearance that turns heads instantly. But behind that wild look is a playful, energetic, and highly intelligent feline. Bengals are incredibly active and require plenty of stimulation—both physical and mental. They love climbing, exploring, and even playing in water, which is rare among cats.",
            "The Exotic Shorthair is often described as the 'lazy man's Persian' due to its similar facial features and sweet temperament, but with a much easier-to-maintain short coat. This breed was created by crossing Persian cats with American Shorthairs, resulting in a plush, teddy bear-like appearance that has captured the hearts of cat lovers around the world. They have large, expressive eyes, a broad flat face, and a cobby body, giving them an irresistibly adorable look. Despite their glamorous appearance, Exotic Shorthairs are extremely affectionate and gentle. They thrive on human companionship and are often happiest when snuggling on a lap or lounging beside their favorite person. ",
            "The Sphynx cat is instantly recognizable for its hairless body, wrinkled skin, and large bat-like ears, making it one of the most unique-looking breeds in the feline world. Despite its lack of fur, the Sphynx is anything but cold or aloof—it is one of the most affectionate, attention-seeking, and playful cat breeds out there. Sphynx cats are known for being extroverted and people-oriented; they crave constant attention and love to be at the center of everything happening in the home. They will follow you around, snuggle under blankets, and even greet guests at the door. These cats are also highly intelligent and curious, enjoying interactive play and learning tricks quickly.",
            "The Birman is a strikingly beautiful cat breed, known for its creamy coat, deep blue eyes, and contrasting white 'gloves' on all four paws. Sometimes referred to as the 'Sacred Cat of Burma', the Birman has a mystical history and a personality that combines grace with affection. Birmans are calm, sweet-natured, and extremely devoted to their human companions. They love being close to people but aren’t overly demanding or clingy. This makes them an excellent choice for families, couples, or individuals seeking a loving and gentle feline friend. Despite their luxurious semi-long coat, Birmans are surprisingly low-maintenance. Their fur is soft, silky, and doesn’t mat easily, so brushing them once or twice a week is usually enough to keep them looking gorgeous.",
            "The Oriental Shorthair is a sleek, stylish, and highly intelligent breed known for its large ears, almond-shaped eyes, and a body structure similar to its cousin, the Siamese. What truly sets the Oriental Shorthair apart is its coat—fine, short, and available in over 300 colors and patterns, including solids, tabbies, torties, and more. This diversity makes them one of the most colorful cat breeds in existence. But it’s not just about looks—Orientals are incredibly vocal, social, and expressive. They love being the center of attention and have no problem letting you know how they feel. Their voices are clear and often used to 'chat' with their humans, especially when they want food, affection, or playtime.",
            "The Persian cat is one of the most beloved and iconic cat breeds, known for its luxurious long coat, flat face, and calm temperament. Originating from Persia (modern-day Iran), these cats have been admired for centuries for their regal appearance and gentle nature. Persian cats have large, expressive eyes—often copper or blue in color—and a short, snub-nosed face that gives them a unique, doll-like look. Their dense, silky fur requires daily grooming to prevent tangles and mats. Available in a wide variety of colors and patterns, Persian cats are typically quiet, affectionate, and enjoy a relaxed indoor lifestyle. They bond closely with their owners and prefer calm environments over loud or chaotic spaces. Despite their royal demeanor, they can be playful when in the mood. ",
        ]
        img_urls = [
            "british_shorthair-cat1.png",
            "Siamese_.cat2.png",
            "doll_.cat3.png",
            "bengal_cat.cat4.png",
            "Exotic_.cat5.png",
            "sphynx_.cat6.png",
            "birman_.cat8.png",
            "shorthair_.cat9.png",
            "percion.cat10.png",
        ]
        image_3d = [
            "british-shorthair-cat1.glb",
            "Siamese.cat2.glb",
            "doll.cat3.glb",
            "bengalcat.cat4.glb",
            "exotic.cat5.glb",
            "Sphynx Cat.cat6.glb",
            "birman.cat8.glb",
            "oriental shorthair.cat9.glb",
            "persion.cat10.glb",
        ]
        
        for title, content, img_urls, image_3d in zip(titles, contents, img_urls, image_3d):
            Post.objects.create(title=title, content=content, img_urls=img_urls, image_3d=image_3d)

        self.stdout.write(self.style.SUCCESS("completed!!!!!!!!!"))