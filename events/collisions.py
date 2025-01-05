from assets.players.player import Player
from assets.objectsPackage.objects import GenericObject
from assets.objectsPackage.objects import Tree

import pygame


def custom_collider_point_using_collider_rect(point, rect: pygame.Rect):
    if not isinstance(point, tuple) or len(point) != 2:
        raise ValueError("The argument must be a tuple with exactly two items.")
    return rect.collidepoint(point)


def custom_collider_using_collider_rect(x, y):
    return x.collider_rect.colliderect(y.collider_rect)


def custom_sprite_collider(player: Player, obstacles: pygame.sprite.Group):
    collided = pygame.sprite.spritecollide(player, obstacles, False, collided=custom_collider_using_collider_rect)
    return collided


def obj_is_adiacet_to_player(obj: GenericObject, player: GenericObject):
    # vertical
    if obj.collider_rect.center[0] + (obj.collider_rect.width / 2) > player.rect.center[0] > obj.collider_rect.center[
        0] - (
            obj.collider_rect.width / 2):
        if (player.rect.center[1] == (
                obj.collider_rect.center[1] - obj.collider_rect.height / 2 - player.collider_rect.height / 2) or
                player.rect.center[1] == (
                        obj.collider_rect.center[1] + obj.collider_rect.height / 2 + player.collider_rect.height / 2)):
            return True

    # horizontal
    if obj.collider_rect.center[1] + (obj.collider_rect.height / 2) > player.rect.center[1] > obj.collider_rect.center[
        1] - (
            obj.collider_rect.height / 2):
        if (player.rect.center[0] == (
                obj.collider_rect.center[0] - obj.collider_rect.width / 2 - player.collider_rect.width / 2) or
                player.rect.center[0] == (
                        obj.collider_rect.center[0] + obj.collider_rect.width / 2 + player.collider_rect.width / 2)):
            return True
    return False
